# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:46:19 2019

@author: khoim
"""

import re
from pandas import ExcelWriter
import pandas                       as pd
#import xlsxwriter

bang=[]
dic=pd.read_csv('dictionary.csv', encoding="ISO-8859-1")
data=pd.read_excel('FB_ML_A.xlsx',index_col=0)
#onegenskill=techskill[0].split(',')
n=len(data.job_description)
#m=len(onegenskill)+1
df = pd.DataFrame({'job_description':data.job_description,
                       })
for i in data.job_description:
        email= re.findall(r'(?:lương|thưởng|salary|bonus|SALARY|LƯƠNG|THƯỞNG|BONUS)\b',i)
        bang.append(email)
df['']=bang

writer = ExcelWriter("Salary.xlsx")
df.to_excel(writer)
writer.save() 
print(bang)