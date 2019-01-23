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
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe")

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
        

  
for i in range (0,100):    
    driver.get("https://vn.indeed.com/jobs?q=Data&start="+str(i)+"0")

    link = driver.find_elements_by_css_selector ('.jobtitle a')
    arrayLink = []
    for i in link:
        j = i.get_attribute('href')
        arrayLink.append(j)
    
    for x in arrayLink:
        driver.get(x)
        driver.implicitly_wait(3)
        try: 
            name = checkElementValue('/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[1]','xp')
            title = checkElementValue('h3', 'css')
            qu=checkElementValue('jobsearch-InlineCompanyRating','class')
            ph=qu.split('\n')
            hihi=ph[2]
            if hihi=='-':
                address=ph[3]
            else:
                address=ph[2]
            ngay = checkElementValue("jobsearch-JobMetadataFooter",'class')
            chia=ngay.split('-')
            ngaypost=chia[1]
            mota = checkElementValue('jobsearch-JobComponent-description', 'class')
        
            ten.append(name)
            theloai.append(title)
            diachi.append(address)
            motacongviec.append(mota)
            postngay.append(ngaypost)

        except: 
            print('Fail: ', x)

df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   #'Salary':tienluong,
                   'Address':diachi,
                   'Detail':motacongviec,
                   'Date':postngay
                   })

writer = ExcelWriter("../../Result/indeed.xlsx")
df.to_excel(writer)
writer.save() 
