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
thongtincongviec1 = []
thongtincongviec2 = []
yeucaucongviec =[]
loiich=[]
tienluong=[]
postngay=[]

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
        

for i in range (1,7):    
    driver.get("https://careerbuilder.vn/viec-lam/data-k-trang-"+str(i)+"-vi.html")

    link = driver.find_elements_by_css_selector ('.job a')
    arrayLink = []
    for i in link:
        j = i.get_attribute('href')
        arrayLink.append(j)
    
    for x in arrayLink:
        driver.get(x)
        driver.implicitly_wait(3)
        try: 
            name = checkElementValue('tit_company', 'class')
            title = checkElementValue('h1', 'tag')
            address = driver.find_element_by_class_name('bgLine1').find_element_by_css_selector('.fl_left a').text
            luong = driver.find_element_by_class_name('bgLine2').find_element_by_class_name('fl_right').text
            thongtin1 = driver.find_element_by_class_name('bgLine2').find_element_by_class_name('fl_left').text
            thongtin2 = driver.find_element_by_class_name('bgLine1').find_element_by_class_name('fl_right').text
            chu = driver.find_elements_by_class_name('MarBot20')
            for i in range(len(chu)):
                j=chu[i].find_element_by_tag_name('h4').text
                if j == "Yêu Cầu Công Việc":
                    yeucau= chu[i].text
                elif j == "Mô tả Công việc":
                    mota= chu[i].text
            ngaypost= checkElementValue('datepost', 'class')
        
            ten.append(name)
            theloai.append(title)
            diachi.append(address)
            motacongviec.append(mota)
            tienluong.append(luong)
            thongtincongviec1.append(thongtin1)
            thongtincongviec2.append(thongtin2)
            yeucaucongviec.append(yeucau)
            postngay.append(ngaypost)

        except: 
            print('Fail: ', x)
    
df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   'Salary':tienluong,
                   'Category1':thongtincongviec1,
                   'Category2':thongtincongviec2,
                   'Address':diachi,
                   'Detail':motacongviec,
                   'Requirement':yeucaucongviec,
                   'Date':postngay
                   })

writer = ExcelWriter("../../Result/careebuilder.xlsx")
df.to_excel(writer)
writer.save() 
