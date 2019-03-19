# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:40:20 2019

@author: khoim
"""

import re
from pandas import ExcelWriter
import pandas                       as pd
#import xlsxwriter

bang=[]
dic=pd.read_csv('dictionary.csv', encoding='ISO-8859-1')
data=pd.read_excel('FB_ML_A.xlsx',index_col=0)
#onegenskill=techskill[0].split(',')
n=len(data.job_description)
#m=len(onegenskill)+1
df = pd.DataFrame({'job_description':data.job_description,
                       })
for i in data.job_description:
        email= re.findall(r'(09|01[2|6|8|9])+([0-9]{8})\b',i)
        bang.append(email)
df['Phone']=bang

writer = ExcelWriter("phone.xlsx")
df.to_excel(writer)
writer.save() 
print(bang)