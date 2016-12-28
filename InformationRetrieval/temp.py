#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:46:03 2016

@author: Takanori
"""

import nltk
import math
import nlph


docs = [
    ["肉", "寿司", "ピザ", "ラーメン", "肉"],
    ["肉","肉","肉","肉"],
    ["寿司","天麩羅","そば","ラーメン","和食", "中心"],
    ["スイーツ","野菜","スイーツ","野菜", "交互"]
]

#tfidfの表示
tfidf_result = nlph.tfidf(docs)
for l in tfidf_result:
    
    print(l)

#ridfの表示





    