from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pandas import ExcelWriter
import pandas                       as pd

bang=[]
dic=pd.read_csv('dictionary.csv')
data=pd.read_excel('jobstreet.xlsx',index_col=0)
print
techskill=dic.technology_skill
onegenskill=techskill[0].split(',')
n=len(data.job_description)+1
m=len(onegenskill)+1
df = pd.DataFrame({'job_description':data.job_description,
                       })
for i in onegenskill:
    danhdau=[]
    for j in range(1,n):
        if i in data.job_description[j] or i.title() in data.job_description[j]:
            dau='x'
        else: dau=''
        danhdau.append(dau)
    df[i]=danhdau

# for i in range(1,m-1):
#     k=onegenskill[i]
#     df = pd.DataFrame({'job_description':data.job_description,
#                        str(k):bang[i],
#                        })

writer = ExcelWriter("test.xlsx")
df.to_excel(writer)
writer.save() 