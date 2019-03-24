# -*- coding: utf-8 -*-

import pandas as pd

a = []
b = []
data = pd.read_excel('', skip_blank_lines=True, skipinitialspace=True) #đọc file dữ liệu gốc
dictionary = pd.read_excel('') #đọc file dictionary
#script = ''
posts = []
for i in range(0,1):     #row mấy tới row cuối
    for skill in dictionary:
        temp = data.loc['i',:]  #điền stt row vô
        if skill in temp and temp not in posts:
            posts.append(temp)
