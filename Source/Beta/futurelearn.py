# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium                          import webdriver
from pandas                            import ExcelWriter
from selenium.webdriver.chrome.options import Options
import pandas                          as pd

chrome_options = Options()
chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)

coursename       = []
timelearn        = []
collaboration    = []


if __name__ == "__main__":
    for i in range(0, 9):
        driver.get('https://www.futurelearn.com/courses/categories/tech-and-coding-courses/data-science')

        link = driver.find_element_by_css_selector('.m-card__title')
        arrayLink = []
        for i in link:
            j = i.get_attribute('href')
            arrayLink.append(j)
        
        for x in arrayLink:
            driver.get(x)       
            try:
                coursename = driver.find_element_by_class_name('m-card__title').text
                timelearn = driver.find_element_by_class_name('m-card__metadata-label').text
                collaboration = driver.find_element_by_class_name('m-card__label').text
            except: 
                print('Fail: ', x)

driver.quit()
  
df = pd.DataFrame({'Course':coursename,
                   'Time':timelearn,
                   'collaboration':collaboration
                   })

writer = ExcelWriter("../../Result/futurelearn.xlsx")

df.to_excel(writer)
writer.save()