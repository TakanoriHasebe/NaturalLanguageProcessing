#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:29:58 2016

@author: Takanori
"""

"""
このプログラムは
自然言語処理(NLP)によく用いられる手法のプログラムが記載されてある
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
    
    def tf(self, sentences):
        
        tf_vocab = {}
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
            #tf_vocab = {}
            for t in sentences_dict.keys():
            
                tf_vocab.update({t : sentences_dict[t]/word_count})
            #print('TFを辞書形式で表した: '+str(tf_vocab))
        
        return tf_vocab
    
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
            
            idf_temp = math.log10(len(sentences)/word_dcount_vocab[t]) + 1
            idf_vocab.update({t: idf_temp})
            
        #print(idf_vocab)
        return idf_vocab

    
'''
tfidfを求める関数

入力例
sentences = [
    ["肉", "寿司", "ピザ", "ラーメン", "肉"],
    ["肉","肉","肉","肉"],
    ["寿司","天麩羅","そば","ラーメン","和食", "中心"],
    ["スイーツ","野菜","スイーツ","野菜", "交互"]    
] 
'''
def tfidf(sentences): #(文章集合, #底#)
    
    #IR_model = IR()
    
    tfidf_vocab_list = []
    
    ############
    #TFの計算開始#
    ############
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
        
        ############
        #TFの計算終了#
        ############
        
        #############
        #IDFの計算開始#
        #############
        
        #TFIDFを算出したい全文章数を求める
        #sentence_number = len(sentences)
        #print('全文章数: '+str(sentence_number))
        
        """ #
        #各文章をわかちがき
        for i in range(len(sentences)):
            
            d[i] = tagger.parse(d[i][0]).split()   
        """ #
        
        #まずは各文章の単語と単語の出現回数の辞書を作成する
        for i in range(len(sentences)):
        
            if i == 0:
                counter = Counter(sentences[i])
                
            else:
                counter += Counter(sentences[i])
        #print('counter: '+str(counter))
        
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
        #print(d_count_list)
        #print(word_list)
        
        #{単語:出現文章数}の辞書の作成
        word_dcount_vocab = dict(zip(word_list, d_count_list))
        #print(word_dcount_vocab)
        
        #print(math.log2(len(d)/word_dcount_vocab['肉']) + 1) #一般的        
        #print(math.log10(len(d)/word_dcount_vocab['肉']) + 1) #Atrae
        #idf = math.log10(len(sentences)/word_dcount_vocab['ピザ']) + 1
        #print('idf: '+str(idf))
        
        #全てのIDFを算出する
        #IDF_temp 
        idf_vocab = {}
        for t in word_dcount_vocab.keys():
            
            idf_temp = math.log10(len(sentences)/word_dcount_vocab[t]) + 1
            idf_vocab.update({t: idf_temp})
                    
        #print('idf_vocab: '+str(idf_vocab))
        #############
        #IDFの計算終了#
        #############
        
        ###############
        #TFIDFの計算開始#
        ###############
        
        #TFIDF = tf_vocab['ピザ'] * idf_vocab['ピザ']
        #print(TFIDF)
        
        #tf_vocab = IR_model.tf(sentences)
        #idf_vocab = IR_model.idf(sentences)
        
        #print(tf_vocab)
        #print(idf_vocab)
        
        tfidf_vocab = {}
        
        for word in set(sentences[n]):
            
            tfidf_temp = tf_vocab[word] * idf_vocab[word]
            tfidf_vocab.update({word : tfidf_temp})
        
            #print('tfidf_vocab: '+str(tfidf_vocab))
    
        tfidf_vocab_list.append(tfidf_vocab)
        ###############
        #TFIDFの計算終了#
        ###############
            
    return tfidf_vocab_list
    
    
'''
ridfを求める関数

入力例
sentences = [
    ["肉", "寿司", "ピザ", "ラーメン", "肉"],
    ["肉","肉","肉","肉"],
    ["寿司","天麩羅","そば","ラーメン","和食", "中心"],
    ["スイーツ","野菜","スイーツ","野菜", "交互"]    
] 
'''        
def ridf(sentences):
    
    pass
    
    

