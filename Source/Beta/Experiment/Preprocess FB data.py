# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:11:28 2019

@author: Tam
"""
import pandas as pd
from pandas import ExcelWriter

ten = []
theloai=[]
diachi = []
motacongviec = []
deadline= []
yeucaucongviec =[]
loiich=[]
tienluong=[]
postngay=[]

data = pd.read_excel('../../../Result/Web/careebuilder.xlsx', skip_blank_lines=True, skipinitialspace=True)
keywords = ['Big Data','Big data','big data','Machine Learning','Machine learning','machine learning','Data Mining','data mining','Hadoop','Pivotal','pivotal',
            'Visualization','visualization','Deep Learning','deep learning','Python','python','Business Intelligence','R Programming','Predictive Modeling','Clustering',
            'Operations Research','Statistician','Graph Database','Data Warehouse','Data Science', 'Data Scientist', 'Data Scientists', 'data scientist',
            'data scientists', 'Data scientist', 'Data scientists', 'data Scientist', 'data Scientists', 'data analyst', 'data analysts', 'Data Analyst',
            'Data Analysts', 'Data analyst', 'Data analysts', 'data Analyst', 'data Analysts', 'data engineer', 'business analyst', 'Data Architect','Statistician',
            'Analytics']#['Tuyển','tuyên','tuyển','TUYỂN']#['Hire','hire','HIRE']
#script = ''
posts = []
for i in range(0, 2251):
    for word in keywords:
        temp = data['Posts'].iloc[i]
        if word in temp and temp not in posts:
            posts.append(temp)
           # script += temp
            data.drop(data.index[i])
df = pd.DataFrame({'post descriptions':posts})
writer = ExcelWriter("../../../Result/Preprocessed IT Jobs and Internship Vietnam.xlsx")
df.to_excel(writer)
writer.save()