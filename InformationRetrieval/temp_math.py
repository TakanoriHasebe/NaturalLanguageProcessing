#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:52:08 2017

@author: Takanori
"""

"""
math
"""

import math
import numpy as np

print(math.log2(2))

print(math.exp(2))

print(1.3010299 + math.log2(1 - math.exp(-0.1)))

#print(math.log2(1 - math.exp(4)))

print(math.exp(2))

#print(math.log2(1 - math.exp(2)))

#print(math.log2(-5))

# value_array = value_array / np.linalg.norm(value_array)

arr = np.array([75, 82])
res = arr / np.linalg.norm(arr)
print(arr)
print(res)

# 辞書の要素をコサイン正規化する
# 対象の辞書
d = {"yamada":75, "endou":82}
# 辞書の要素を抜き出し, コサイン正規化し, 新しいリストの作成
value_list = list(d.values()) / np.linalg.norm(list(d.values()))
# 辞書から単語を抜き出し, 単語のリストを作成
word_list = list(d.keys())
print(word_list)
# 辞書にコサイン類似度で算出した値を入れる
for i in range(len(word_list)):
    
    d[word_list[i]] = value_list[i]
# コサイン正規化された
print("コサイン正規化された辞書の表示: "+str(d))





