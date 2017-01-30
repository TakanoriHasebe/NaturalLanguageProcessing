#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:46:03 2016

@author: Takanori
"""

import nltk
import math
import InformationRetrieval as ir
import codecs
import MeCab

# 各文章から名詞を抜き出してきたもの
docs = [
    ["肉", "寿司", "ピザ", "ラーメン", "肉"], # 1番目の文章
    ["肉","肉","肉","肉"], # 2番目の文章
    ["寿司","天麩羅","そば","ラーメン","和食", "中心"], # 3番目の文章
    ["スイーツ","野菜","スイーツ","野菜", "交互"] # 4番目の文章
]

# docsの表示
# print(docs)

# tfidfの表示
tfidf_result = ir.tfidf(docs)

# 代入したdocsのtfidfの表示
for l in tfidf_result:
    
    print(l)




    