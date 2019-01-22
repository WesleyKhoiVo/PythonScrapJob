# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:17:21 2019

@author: khoim
"""

from selenium                          import webdriver
from pandas                            import ExcelWriter
from selenium.webdriver.chrome.options import Options
import pandas                          as pd

chrome_options = Options()
chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)

coursename       = []

if __name__ == "__main__":
    for i in range(0, 9):
        driver.get('https://alison.com/courses/data-science')
        link = driver.find_element_by_class_name('course-block-intro')
        arrayLink = []
        for i in link:
            j = i.get_attribute('href')
            arrayLink.append(j)
        
        for x in arrayLink:
            driver.get(x)       
            try:                
                coursename = driver.find_element_by_class_name('course-block-content').text
            except: 
                print('Fail: ', x)

driver.quit()
  
df = pd.DataFrame({'Course':coursename
                   })

writer = ExcelWriter("../../Result/alison.xlsx")


df.to_excel(writer)
writer.save()