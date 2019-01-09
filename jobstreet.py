# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pandas import ExcelWriter
import pandas                       as pd

option = webdriver.ChromeOptions()
option.add_argument(' - incognito')

driver = webdriver.Chrome()
driver.get("https://www.jobstreet.vn/j?q=data&l=&sp=homepage")

#elem = driver.find_element_by_xpath('//*[@id="job-mail-subscribe-modal"]/div/div/div/button/span')
#elem.click()
#timeout=20

ten = []
theloai=[]
diachi = []
motacongviec = []
yeucaukinhnghiem =[]
loiich=[]
count = 0
link = driver.find_elements_by_class_name('jobtitle')

#form1
while count <10:
    for i in link:
        j = i.get_attribute('href')
        driver.get(j)
        name = driver.find_element_by_id('company_name').text
        title = driver.find_element_by_('position_title').text
        address = driver.find_element_by_id('address').text
        mota = driver.find_element_by_class_name('job_description').text
        experience = driver.find_element_by_id('years_of_experience').text
        lido = driver.find_element_by_class_name('why_join_us_all').text
        
        ten.append(name)
        theloai.append(title)
        diachi.append(address)
        motacongviec.append(mota)
        yeucaukinhnghiem.append(experience)
        loiich.append(lido)
        count = count+1


#form2       
# while count <10:
    for i in link:
        j = i.get_attribute('href')
        driver.get(j)
        name = driver.find_element_by_class_name ('company').text
        title = driver.find_element_by_tag_name('h1').text
        address = driver.find_element_by_class_name('location').text
        mota = driver.find_element_by_class_name('summary').text
        thoigian = driver.find_element_by_class_name('date').text
        #lido = driver.find_element_by_class_name('why_join_us_all').text
        
        ten.append(name)
        theloai.append(title)
        diachi.append(address)
        motacongviec.append(mota)
        yeucaukinhnghiem.append(thoigian)
        #loiich.append(lido)
        count = count+1
        

df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   'Address':diachi,
                   'Job':motacongviec,
                   'Year-Experience':yeucaukinhnghiem,
                   'benifit':loiich
                   })

writer = ExcelWriter("jobstreet.xlsx")
df.to_excel(writer)
writer.save() 
