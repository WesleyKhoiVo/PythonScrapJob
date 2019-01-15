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
driver = webdriver.Chrome(executable_path=r'C:\Users\Tam\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')

ten = []
theloai=[]
diachi = []
motacongviec = []
kinhnghiemcongviec = []
loiichcongviec= []
#yeucaucongviec =[]
tienluong=[]
postngay=[]
count=0

def checkElementValue(element, typeGet): 
    try:
        if typeGet == 'id':
            return driver.find_element_by_id(element).text
        elif typeGet == 'class': 
            return driver.find_element_by_class_name(element).text
        elif typeGet == 'tag':
            return driver.find_element_by_tag_name(element).text
        elif typeGet == 'css':
            return driver.find_element_by_css_selector(element).text
        elif typeGet == 'xp':
            return driver.find_element_by_xpath(element).text
    except:
        return ''
        

  
for i in range (1,4):    
    driver.get("https://itviec.com/it-jobs/data?page="+str(i))

    link = driver.find_elements_by_css_selector ('.title a')
    arrayLink = []
    for i in link:
        j = i.get_attribute('href')
        arrayLink.append(j)
    
    for x in arrayLink:
        driver.get(x)
        driver.implicitly_wait(3)
        try: 
            name = checkElementValue('name', 'class')
            title = checkElementValue('job_title', 'class')
            address =checkElementValue('address__full-address','class')
            lido = checkElementValue('top-3-reasons','class')
            mota = checkElementValue('description','class')
            kinhnghiem = checkElementValue('experience','class')
            loiich = checkElementValue("culture_description",'class')
            ngaypost= checkElementValue('distance-time-job-posted highlight', 'class')
        
            ten.append(name)
            theloai.append(title)
            diachi.append(address)
            motacongviec.append(mota)
            #tienluong.append(luong)
            kinhnghiemcongviec.append(kinhnghiem)
            loiichcongviec.append(loiich)
            #yeucaucongviec.append(yeucau)
            postngay.append(ngaypost)

        except: 
            print('Fail: ', x)

df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   #'Salary':tienluong,
                   'Address':diachi,
                   'Detail':motacongviec,
                   'Experience':kinhnghiemcongviec,
                   'Benefic':loiichcongviec,
                   'Date':postngay
                   })

writer = ExcelWriter("itviec.xlsx")
df.to_excel(writer)
writer.save() 
