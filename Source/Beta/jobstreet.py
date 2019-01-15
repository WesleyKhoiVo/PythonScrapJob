# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 07:44:03 2019

@author: lengoyenphuong
"""
from selenium                          import webdriver
from pandas                            import ExcelWriter
from selenium.webdriver.chrome.options import Options
import pandas                          as pd

chrome_options = Options()
chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)

ten              = []
theloai          = []
diachi           = []
motacongviec     = []
yeucaukinhnghiem = []
thoigianpost     = []

def checkElementValue(element, typeGet): 
    try:
        if typeGet == 'id':
            return driver.find_element_by_id(element).text
        return driver.find_element_by_class_name(element).text
    except:
        return ''

for i in range (1,50):    
    driver.get("https://www.jobstreet.vn/j?l=&p=" + str(i) + "&q=data&sp=homepage")

    link = driver.find_elements_by_class_name('jobtitle')
    arrayLink = []
    for i in link:
        j = i.get_attribute('href')
        arrayLink.append(j)
    
    for x in arrayLink:
        driver.get(x)
        # driver.implicitly_wait(0.5)
        
        try: 
            try:
                name = checkElementValue('company_name', 'id')
                title = driver.find_element_by_id('position_title').text
                address = driver.find_element_by_id('address').text
                mota = driver.find_element_by_id('job_description').text
                experience = driver.find_element_by_id('years_of_experience').text
                thoigian = ''      
            except:
                name = checkElementValue('company', 'class')
                title = driver.find_element_by_tag_name('h1').text
                address = driver.find_element_by_class_name('location').text
                mota = driver.find_element_by_class_name('summary').text
                thoigian = driver.find_element_by_class_name('date').text
                experience = ' '
                
            ten.append(name)
            theloai.append(title)
            diachi.append(address)
            motacongviec.append(mota)
            yeucaukinhnghiem.append(experience)
            thoigianpost.append(thoigian)
        except: 
            print('Fail: ', x)

driver.quit()
  
df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   'Address':diachi,
                   'Job':motacongviec,
                   'Year-Experience':yeucaukinhnghiem,
                   'Time':thoigianpost
                   })

writer = ExcelWriter("../../Result/jobstreet.xlsx")


df.to_excel(writer)
writer.save()