# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:08:16 2019

@author: Khoi
"""

import pickle

with open('./regex.dict.pkl', 'rb') as f:
    data = pickle.load(f)
    
phone = data['phone']
print(phone)
print('\n')
emojie = data['emojie']
print(emojie)
print('\n')
url = data['url']
print(url)
print('\n')
mail = data['mail']
print(mail)