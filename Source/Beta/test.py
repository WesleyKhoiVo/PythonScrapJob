from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pandas import ExcelWriter
import xlwt
from xlwt import Workbook
import pandas                       as pd

option = webdriver.ChromeOptions()
option.add_argument(' - incognito')

driver = webdriver.Chrome()
driver.get("https://itviec.com/it-jobs/data")

elem = driver.find_element_by_xpath('//*[@id="job-mail-subscribe-modal"]/div/div/div/button/span')
elem.click()
timeout=20

ten = []
theloai=[]
diachi = []
lido = []
kinhnghiem =[]
loiich=[]

#0
link = driver.find_element_by_xpath('//*[@id="job_45590"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)

driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45634"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)

driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45846"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45758"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45724"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45704"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45633"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45624"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45787"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)

driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45069"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45066"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45038"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_45353"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44832"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44697"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44730"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44719"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44786"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)


driver.get("https://itviec.com/it-jobs/data")
link = driver.find_element_by_xpath('//*[@id="job_44905"]/div/div[2]/div[1]/div/h2/a').get_attribute('href')
driver.get(link)
name = driver.find_element_by_class_name('name').text
title = driver.find_element_by_class_name('job_title').text
address = driver.find_element_by_class_name('address__full-address').text
reason = driver.find_element_by_class_name('top-3-reasons').text
experience = driver.find_element_by_class_name('experience').text
benifit = driver.find_element_by_class_name('culture_description').text
ten.append(name)
theloai.append(title)
diachi.append(address)
lido.append(reason)
kinhnghiem.append(experience)
loiich.append(benifit)



df = pd.DataFrame({'Name':ten,
                   'Title':theloai,
                   'address':diachi,
                   'reason':lido,
                   'experience':kinhnghiem,
                   'benifit':loiich
                   })

writer = ExcelWriter("thulan2.xlsx")
df.to_excel(writer)
writer.save() 



