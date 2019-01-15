# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:13:59 2019

@author: khoi.vominh
"""

from selenium                          import webdriver
from selenium.common.exceptions        import TimeoutException
from selenium.webdriver.common.keys    import Keys
from selenium.webdriver.chrome.options import Options
from bs4                               import BeautifulSoup
from datetime                          import datetime, timedelta
from pandas                            import ExcelWriter
import pandas                          as pd
import numpy                           as np
import requests

username = "khoiminhvo1996@hotmail.com" 
password = "Khoi1996"

def init_driver():
    chrome_options = Options()
    chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
    driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)
    return driver

def login(driver, username, password):
    driver.get("http://www.glassdoor.com/profile/login_input.htm")
    try:
        user_field = driver.find_element_by_name("username")
        pw_field = driver.find_element_by_name("password")
        login_button = driver.find_element_by_xpath('//button[@class="gd-btn gd-btn-1 fill"]')
        user_field.send_keys(username)
        user_field.send_keys(Keys.TAB)
        pw_field.send_keys(password)
        login_button.click()
    except TimeoutException:
        print("TimeoutException! Username/password field or login button not found on glassdoor.com")

def search(driver, city, title):
    driver.get("https://www.glassdoor.com/index.htm")
    try:
        title_field = driver.find_element_by_id("KeywordSearch")
        city_field = driver.find_element_by_id("LocationSearch")
        title_field.send_keys(title)
        title_field.send_keys(Keys.TAB)
        city_field.send_keys(city)
        city_field.send_keys(Keys.RETURN)
    except TimeoutException:
        print("TimeoutException! city/title field or search button not found on glassdoor.com")

def get_position_link(url):
    links = []
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url,headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find_all('a', class_='jobLink')
    for i in a:
        links.append('https://www.glassdoor.com' + i.get('href'))
    return links

def get_all_links(num_page, url):
    link = []
    i = 1
    while i <= num_page:
        try:
            url_main = url + str(i) + '.htm'
            link.append(get_position_link(url_main))
            i = i + 1
        except:
            print('No more pages found.')
    return link

def scrap_job_page(url):
    dic = {}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('body')
    try:
        dic['job_title'] = body.find('h2', class_='noMargTop margBotXs strong').text.strip()
    except:
        dic['job_title'] = np.nan

    try:
        dic['company_name'] = body.find('span', class_='strong ib').text.strip()
    except:
        dic['company_name'] = np.nan

    try:
        location = body.find('span', class_='subtle ib').text.strip().replace('–\xa0', '')
        dic['location'] = location
    except:
        dic['location'] = np.nan

    try:
        dic['salary_estimated'] = body.find('h2', class_='salEst').text.strip()
    except:
        dic['salary_estimated'] = np.nan

    try:
        dic['salary_min'] = body.find('div', class_='minor cell alignLt').text.strip()
    except:
        dic['salary_min'] = np.nan

    try:
        dic['salary_max'] = body.find('div', class_='minor cell alignRt').text.strip()
    except:
        dic['salary_max'] = np.nan

    try:
        date = body.find('span', class_='minor nowrap').text.strip()
        split = date.split(" ")
        if "second" in split or "seconds" in split:
            dic["date_posted"] = datetime.today().date()
        if "minute" in split or "minutes" in split:
            dic["date_posted"] = datetime.today().date()
        if "hours" in split or "hour" in split:
            dic["date_posted"] = datetime.today().date()
        if "week" in split or "weeks" in split:
            dic["date_posted"] = (datetime.today() - (timedelta(days=int(split[0]) * 7))).date()
        if "days" in split or "day" in split:
            dic["date_posted"] = (datetime.today() - timedelta(days=int(split[0]))).date()
        if "month" in date or "months" in date:
            dic["date_posted"] = (datetime.today() - (timedelta(days=int(split[0]) * 30))).date()
    except:
        dic["date_posted"] = datetime.today().date()
        
    list_skills = []
    job_des = body.find('div', class_='jobDesc')

    for i in job_des:
        try:
            for li in i.find_all("li"):
                list_skills.append(li.text.strip())
        except:
            break
    try:
        dic['job_description'] = list_skills
    except:
        dic['job_description'] = np.nan

    return dic

if __name__ == "__main__":
    links = []
    driver = init_driver()
    login(driver, username, password)
    data_out = []
    city = "Ho Chi Minh"
    search(driver, city, 'data')
    url = driver.current_url
    links = get_all_links(15, url)
    flatten = [item for sublist in links for item in sublist]
    remove_duplicates = list(set(flatten))
    list_result = []
    for page in remove_duplicates:
        try:
            list_result.append(scrap_job_page(page))
        except:
            pass
    
    df = pd.DataFrame.from_dict(list_result)

    writer = ExcelWriter('../../Result/glassdoor.xlsx')
    df.to_excel(writer, index=False)
    df.to_excel(writer, startrow=len(df) + 2, index=False)
    writer.save()    
    driver.quit()