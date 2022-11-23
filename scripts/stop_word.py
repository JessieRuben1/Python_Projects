# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:27:47 2020

@author: admin
"""


import pandas as pd
import numpy
import csv
import nltk
from nltk.tokenize import word_tokenize
import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


train_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\train.csv")
test_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\test.csv")

sentence1 = str(train_file[['tweet']])

stop_words = set(stopwords.words("english"))

words=word_tokenize(sentence1)
filtered_sentence = [w for w in words if not w in stop_words]

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

print(filtered_sentence)