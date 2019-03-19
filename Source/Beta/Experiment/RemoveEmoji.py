# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:13:53 2019

@author: khoim
"""

import re

text = u'This dog 😂'

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
print(emoji_pattern.sub(r'', text)) # no emoji

s = '😀'
print('U000{:X}'.format(ord(s)))