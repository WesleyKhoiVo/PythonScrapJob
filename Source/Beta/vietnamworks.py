# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:46:13 2019

@author: khoi.vominh
"""

from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys    import Keys
from selenium.common.exceptions        import TimeoutException

username = "khoiminhvo1996@hotmail.com" 
password = "Khoi1996"

def init_driver():
    chrome_options = Options()
    chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
    driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)
    return driver

def login(driver, username, password):
    driver.get("https://secure.vietnamworks.com/login/vi?client_id=3")
    try:
        user_field = driver.find_element_by_name("username")
        pw_field = driver.find_element_by_name("password")
        login_button = driver.driver.find_element_by_xpath('//input[@id="button-login"]')
        user_field.send_keys(username)
        user_field.send_keys(Keys.TAB)
        pw_field.send_keys(password)
        login_button.click()
    except TimeoutException:
        print("TimeoutException!")

def search(driver, city, title):
    driver.get("https://www.vietnamworks.com/data-kv")
    try:
        name = driver.find_elements_by_xpath('//h1[@itemprop="title"]/text()')
        company = driver.find_elements_by_xpath('//span[@class="company-name text-lg block"]/strong/text()')
        address = driver.find_elements_by_xpath('//span[@class="company-address block"]/text()')
        city = driver.find_elements_by_xpath('//span[@itemprop="address"]/a/text()')
        wage = driver.find_elements_by_xpath('//span[@class="orange bold-700 text-lg"]/text()')
        work= driver.find_elements_by_xpath('//div[@id="job-description"]/text()')
        information = driver.find_elements_by_xpath('//span[@id="companyprofile"]/text()')
        
        
        
    except TimeoutException:
        print("TimeoutException!")


if __name__ == "__main__":
    links = []
    driver = init_driver()
    login(driver, username, password)
    