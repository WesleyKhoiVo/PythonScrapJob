# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:44:10 2019

@author: khoim
"""

import json
from pprint import pprint

with open('emojis.json', encoding = "utf8") as data_file:
    data = json.load(data_file)
    
pprint(data['emojis'])