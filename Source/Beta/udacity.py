# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium                          import webdriver
from pandas                            import ExcelWriter
from selenium.webdriver.chrome.options import Options
import pandas                          as pd
import time

chrome_options = Options()
chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)

coursename       = []
level            = []
category         = []
skill            = []
collaboration    = []


if __name__ == "__main__":
    for i in range(0, 30):
        driver.get('https://www.udacity.com/courses/school-of-data-science')
        time.sleep(5)
        driver.find_element_by_css_selector('.modal-close.white-shadow').click()
        link = driver.find_element_by_css_selector('.card-wrapper.is-collapsed')
        arrayLink = []
        for i in link:
            j = i.get_attribute('href')
            arrayLink.append(j)
        
        for x in arrayLink:
            driver.get(x)       
            try:
                category = driver.find_element_by_class_name('category ng-star-inserted').text
                coursename = driver.find_element_by_class_name('card-heading').text
                level = driver.find_element_by_class_name('capitalize').text
                collaboration = driver.find_element_by_class_name('hidden-sm-down ng-star-inserted').text
                skill = driver.find_element_by_class_name('skills ng-star-inserted').text
            except: 
                print('Fail: ', x)

driver.quit()
  
df = pd.DataFrame({'Course':coursename,
                   'Category':category,
                   'level':level,
                   'collaboration':collaboration,
                   'Skill':skill
                   })

writer = ExcelWriter("../../Result/udacity.xlsx")


df.to_excel(writer)
writer.save()