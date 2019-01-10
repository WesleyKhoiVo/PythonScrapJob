# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 07:44:03 2019

@author: khoim
@co-author: Tam
"""
import time
import pandas                       as pd

from selenium                       import webdriver
from pandas                         import ExcelWriter
from selenium.webdriver.support.ui  import WebDriverWait

# driver = webdriver.Chrome(r"C:\Users\khoim\Documents\PortableApps\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/groups/740288779351180/")

startscript    = time.time()
countAccept    = 0
countFail      = 0

posts      = []



links      = []
times      = []
scripts    = []
mores      = []
duplicates = []
hours      = []
mins       = []
days       = []
months     = []
years      = []
ids        = []

num           = 0
frnum         = 0
key           = 0
duplicatesAll = 0

while frnum < 10000:
    try:
        links   = driver.find_elements_by_xpath('//div[@data-ad-preview="message"]')
        times   = driver.find_elements_by_xpath('//a[@class="_5pcq"]//abbr')
        scripts = driver.find_elements_by_xpath('//a[@class="_5pcq"]')
        mores   = driver.find_elements_by_xpath('//div[@data-ad-preview="message"]//a[@class="see_more_link"]')

        for more in mores[num:]:
            more.click()
        num = len(mores)
        
        for i in range(frnum,min(min(len(links), len(times)), len(scripts))):
            start = time.time()
            link = links[i]
            postTime = times[i].get_attribute("title")
            idp = scripts[i].get_attribute("href").split('/')[-2]
            count = 1
            while count>0:
                try:
                    if link.text in posts: 
                        idx = posts.index(link.text)

                        try:
                            int(idp[0])
                        except:
                            idp = -1
                    
                        if (idp in ids and idp != -1):
                                duplicatesAll += 1
                                print("Post thứ {0:3} bị trùng trong {1:4.0f} ms ".format(duplicatesAll,(time.time()-start)*1000))
                                break

                        duplicates.append(idx)
                    else:
                        duplicates.append(-1)

                    posts.append(link.text)

                    hours.append(int(postTime.split(',')[0].split(':')[0]))
                    mins.append(int(postTime.split(',')[0].split(':')[1]))
                    days.append(int(postTime.split(',')[1].split('/')[0]))
                    months.append(int(postTime.split(',')[1].split('/')[1]))
                    years.append(int(postTime.split(',')[1].split('/')[2]))
                    ids.append(str(idp))

                    print("Post thứ {0:3} lấy thành công trong {1:4.0f} ms ".format(countFail + len(posts), (time.time() - start) * 1000))
                    countAccept += 1

                    break

                except:
                    if count == 1:
                        countFail += 1
                    count += 1
                    print("Post thứ {0:3} lấy thất bại lần thứ {2} tronge {1:4.0f} ms ".format(i + 1, (time.time() - start) * 1000, count))
                    if count > 3: 
                        break
        frnum = min(min(len(links), len(times)), len(scripts))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        key = 1
        break       
        
driver.quit()

print("Post đã có : ", len(posts))
print("Post lấy thành công : ", countAccept)
print("Post lấy thất bại : ", countFail)
print("Tổng thời gian thực hiện : {:7.6} s".format(time.time() - startscript))
print("Tổng trung bình lấy 1 post : {:7.6} s".format((time.time() - startscript) / max(countAccept, 1)))


df = pd.DataFrame({'Id':ids,
                   'Posts':posts,
                   'Duplicates':duplicates,
                   'Hours':hours,
                   'Mins':mins,
                   'Days':days,
                   'Months':months,
                   'Years':years,
                   })

writer = ExcelWriter("Học máy và ứng dụng.xlsx")
df.to_excel(writer)
writer.save()