# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 07:44:03 2019

@author: khoim
"""

import pandas                          as pd

from selenium                          import webdriver
from pandas                            import ExcelWriter
from selenium.webdriver.chrome.options import Options

site = input('Input facebook site group: ')
chrome_options = Options()
chrome_options.add_extension(r'../../Tools/ublock_extension.crx')
driver = webdriver.Chrome(r"../../Tools/chromedriver.exe", options = chrome_options)
driver.get(site)

posts      = []
links      = []
times      = []
scripts    = []
mores      = []
hours      = []
mins       = []
days       = []
months     = []
years      = []
ids        = []

num        = 0
frnum      = 0

while frnum < 1000:
    try:
        
        # get element
        links   = driver.find_elements_by_xpath('//div[@data-ad-preview="message"]')
        times   = driver.find_elements_by_xpath('//a[@class="_5pcq"]//abbr')
        scripts = driver.find_elements_by_xpath('//a[@class="_5pcq"]')
        mores   = driver.find_elements_by_xpath('//div[@data-ad-preview="message"]//a[@class="see_more_link"]')

        for more in mores[num:]:
            more.click()
        num = len(mores)
        
        for i in range(frnum,min(min(len(links), len(times)), len(scripts))):
            
            link = links[i]
            postTime = times[i].get_attribute("title")
            idp = scripts[i].get_attribute("href").split('/')[-2]
            
            # get post with some 
            count = 1
            while count > 0:
                try:
                    # get index
                    if link.text in posts: 
                        idx = posts.index(link.text)                           

                    # set index post, remove some post is ad
                    int(idp[0])
                    posts.append(link.text)

                    #data split
                    ids.append(str(idp))
                    hours.append(int(postTime.split(',')[0].split(':')[0]))
                    mins.append(int(postTime.split(',')[0].split(':')[1]))
                    days.append(int(postTime.split(',')[1].split('/')[0]))
                    months.append(int(postTime.split(',')[1].split('/')[1]))
                    years.append(int(postTime.split(',')[1].split('/')[2]))

                    break

                
                except:
                    count += 1
                    if count > 3: 
                        break
                    
        frnum = min(min(len(links), len(times)), len(scripts))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    except:
        break       
        
driver.quit()

print("Post đã có : ", len(posts))

df = pd.DataFrame({'Id':ids,
                   'Posts':posts,
                   'Hours':hours,
                   'Mins':mins,
                   'Days':days,
                   'Months':months,
                   'Years':years,
                   })

writer = ExcelWriter("../../Result/IT Jobs and Internship Vietnam_Data Science Only.xlsx")
df.to_excel(writer)
writer.save()