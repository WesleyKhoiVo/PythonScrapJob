# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:11:28 2019

@author: Tam
"""
import pandas as pd
from pandas import ExcelWriter

website = []
tencongty = []
tencongviec = []
theloai=[]
diachi = []
motacongviec = []
deadline= []
yeucaucongviec =[]
loiich=[]
tienluong=[]
ngaypost=[]
ngayend=[]
data = pd.read_excel('../../../Result/Web/Web Data.xlsx', skip_blank_lines=True, skipinitialspace=True)
keywords = ['Big Data','Big data','big data','Machine Learning','Machine learning','machine learning','Data Mining','data mining','Hadoop','Pivotal','pivotal',
            'Visualization','visualization','Deep Learning','deep learning','Python','python','Business Intelligence','R Programming','Predictive Modeling','Clustering',
            'Operations Research','Statistician','Graph Database','Data Warehouse','Data Science', 'Data Scientist', 'Data Scientists', 'data scientist',
            'data scientists', 'Data scientist', 'Data scientists', 'data Scientist', 'data Scientists', 'data analyst', 'data analysts', 'Data Analyst',
            'Data Analysts', 'Data analyst', 'Data analysts', 'data Analyst', 'data Analysts', 'data engineer', 'business analyst', 'Data Architect','Statistician',
            'Analytics']#['Tuyển','tuyên','tuyển','TUYỂN']#['Hire','hire','HIRE']
#script = ''
posts = []
for i in range(0, 2088):
    for word in keywords:
        temp = data['Detail'].iloc[i]
        if word in temp and temp not in posts:
            posts.append(temp)
            website.append(data['Website'].iloc[i])
            tencongty.append(data['Name'].iloc[i])
            tencongviec.append(data['Title'].iloc[i])
            tienluong.append(data['Salary'].iloc[i])
            diachi.append(data['Location'].iloc[i])
            motacongviec.append(data['Detail'].iloc[i])
            yeucaucongviec.append(data['Requirement'].iloc[i])
            loiich.append(data['Benefits'].iloc[i])
            ngaypost.append(data['Date Post'].iloc[i])
            ngayend.append(data['End Date'].iloc[i])
           # script += temp
            data.drop(data.index[i])
df = pd.DataFrame({'Website':website,
                    'Company':tencongty,
                   'Job Title':tencongviec,
                   'Salary':tienluong,
                   'Location':diachi,
                   'Detail':motacongviec,
                   'Requirement':yeucaucongviec,
                   'Post Date':ngaypost,
                   'End Date':ngayend
                   })
writer = ExcelWriter("../../../Result/Preprocessed Web Data.xlsx")
df.to_excel(writer)
writer.save()