# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pandas import ExcelWriter
import pandas                       as pd


# driver firefox
#driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe')

# driver = webdriver.Chrome()
#ChromeOptions = webdriver.ChromeOptions()
#ChromeOptions.add_argument('--disable-browser-side-navigation')
#ChromeOptions.add_argument(' - incognito')
driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')

ten= []
theloai=[]
diachi= []
motacongviec= []
yeucaukinhnghiem=[]
#loiich=[]
thoigianpost=[]
count = 0

def checkElementValue(element, typeGet): 
    try:
        print('element, typeGet ===> ', element, typeGet);
        if typeGet == 'id':
            return driver.find_element_by_id(element).text
        else if typeGet == 'class': 
            return driver.find_element_by_class_name(element).text
        else if typeGet == 'tag':
            return driver.find_element_by_tag_name(element).text
    except:
        return ''
        

for i in range (1,2):    
    driver.get("https://www.jobstreet.vn/j?l=&p="+str(i)+"&q=data&sp=homepage")

    link = driver.find_elements_by_class_name('jobtitle')
    arrayLink = []
    for i in link:
        j = i.get_attribute('href')
        arrayLink.append(j)
    
    for x in arrayLink:
        driver.get(x)
        driver.implicitly_wait(3)
        try: 
            try:
                #name = driver.find_element_by_id('company_name').text
                name = checkElementValue('company_name', 'id')
                title = checkElementValue('position_title', 'id')
                address = checkElementValue('address', 'id')
                mota = checkElementValue('job_description', 'id')
                experience = checkElementValue('years_of_experience', 'id')
                thoigian = ''
                print ('name_1: ', name)
                print('1: ', x)       
            except:
                #name = driver.find_element_by_class_name('company').text
                name = checkElementValue('company', 'class')
                title = checkElementValue('h1', 'tag')
                address = checkElementValue('location', 'class')
                mota = checkElementValue('summary', 'class')
                thoigian = checkElementValue('date', 'class')
                experience = ''
                print ('name_2: ', name)
                print('2: ', x)
                
            ten.append(name)
            theloai.append(title)
            diachi.append(address)
            motacongviec.append(mota)
            yeucaukinhnghiem.append(experience)
            thoigianpost.append(thoigian)
        except: 
            print('Fail: ', x)
    
df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   'Address':diachi,
                   'Job':motacongviec,
                   'Year-Experience':yeucaukinhnghiem,
                   'Time':thoigianpost
                   })

writer = ExcelWriter("jobstreet.xlsx")
df.to_excel(writer)
writer.save() 



