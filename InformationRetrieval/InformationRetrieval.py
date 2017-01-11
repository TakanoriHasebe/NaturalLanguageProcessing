#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:29:58 2016

@author: Takanori
"""

"""
このプログラムは
自然言語処理(NLP)によく用いられる手法のプログラムが記載されてある

主に情報検索技術に用いられるプログラムが記述してある
"""

import numpy as np
import pandas as pd
import MeCab
from collections import Counter
import math

tagger = MeCab.Tagger('-Owakati')

'''
情報検索などで用いられるクラスの作成

information retrieval
'''
class IR():
    
    #Term Frequencyを算出する関数
    def tf(self, sentences):
        
        tf_vocab_list = []
        for n in range(len(sentences)):
        
            #print(n)
            #入力された文章をわかち書きしている
            #sentences_wakati_list = tagger.parse(sentences).split() #
            sentences_wakati_list = sentences[n]
            #print(sentences_wakati_list)  
            
            #文章内（その文）での全単語数
            word_count = len(sentences_wakati_list)
            #print('文章内での単語数: '+str(word_count))
            
            #各単語が文章内に何回出てきているかの辞書を作成
            sentences_dict = Counter(sentences_wakati_list)
            #print('各単語の出現頻度の辞書: '+str(sentences_dict))
            
            #TFを辞書形式で保存
            tf_vocab = {}
            for t in sentences_dict.keys():
            
                tf_vocab.update({t : sentences_dict[t]/word_count})
            #print('TFを辞書形式で表した: '+str(tf_vocab))
            tf_vocab_list.append(tf_vocab)
        
        return tf_vocab_list
    
    #Inverse Document Frequencyを算出する関数
    def idf(self, sentences):
        
        #まずは各文章の単語と単語の出現回数の辞書を作成する
        for i in range(len(sentences)):
        
            if i == 0:
                counter = Counter(sentences[i])
                
            else:
                counter += Counter(sentences[i])
                
        
        #各単語が出現するドキュメント数, 各単語の抜き出し
        d_count_list = []
        word_list = []
        for t in counter.keys():
            d_count = 0
            for i in range(len(sentences)):
                for j in range(len(sentences[i])):
                    
                    if t == sentences[i][j]:
                        d_count += 1
                        break
            
            d_count_list.append(d_count)
            word_list.append(t)
            
        #{単語:出現文章数}の辞書の作成
        word_dcount_vocab = dict(zip(word_list, d_count_list))
        
        #全てのIDFを算出する
        #IDF_temp 
        idf_vocab = {}
        for t in word_dcount_vocab.keys():
            
            #ここでlogの底を2, eなどに変えることで結果も変わる
            idf_temp = math.log10(len(sentences)/word_dcount_vocab[t]) + 1
            idf_vocab.update({t: idf_temp})
            
        #print(idf_vocab)
        return idf_vocab

'''
TF-IDFを算出する関数
入力するsentencesは１文が分かち書きされており, １つの配列に単語が要素として入っている

入力例
sentences = [
    ["肉", "寿司", "ピザ", "ラーメン", "肉"],
    ["肉","肉","肉","肉"],
    ["寿司","天麩羅","そば","ラーメン","和食", "中心"],
    ["スイーツ","野菜","スイーツ","野菜", "交互"]    
] 
'''
def tfidf(sentences):
    
    ir = IR()
    
    #最終結果を返すリスト
    tfidf_vocab_list = []
    
    #sentencesを代入してTerm Frequencyを算出
    tf_vocab_list = ir.tf(sentences)
    
    #sentencesを代入してinverse document frequencyを算出
    idf_vocab = ir.idf(sentences)
    
    #TFIDFの算出
    tfidf_vocab_list = []
    for i in range(len(sentences)):
        tfidf_vocab = {}
        for j in range(len(sentences[i])):
            tfidf_vocab.update({sentences[i][j] : tf_vocab_list[i][sentences[i][j]]*idf_vocab[sentences[i][j]] })
        #print(tfidf_vocab)
        tfidf_vocab_list.append(tfidf_vocab)
        
    return tfidf_vocab_list        
        
'''
R-IDFを算出する関数

入力例
TF-IDFと同様の入力にする
'''
def ridf(sentences):
    
    ir = IR()
    
    #最終結果を返すリスト
    ridf_vocab_list = []
    
    #sentencesを代入してTerm Frequencyを算出
    tf_vocab_list = ir.tf(sentences)
    
    #sentencesを代入してinverse document frequencyを算出
    idf_vocab = ir.idf(sentences)
    
    #print('tf_vocab_list: '+str(tf_vocab_list))
    #print(' ')
    #print('idf_vocab: '+str(idf_vocab))
        
    #R-IDFの算出
    ridf_vocab = {}
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            
            ridf_vocab[sentences[i][j]] = idf_vocab[sentences[i][j]] + math.log2(1 - math.exp(-(tf_vocab_list[i][sentences[i][j]]/len(sentences))))
            #print(sentences[i][j], ridf_vocab)
        ridf_vocab_list.append(ridf_vocab)
        ridf_vocab = {} #初期化
        
    #print(ridf_vocab_list)
    return ridf_vocab_list
    
    
    
    
    
    
    
    
    