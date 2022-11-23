# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:02:42 2020

@author: admin
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

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


sentence=str(train_file[['tweet']])
words = word_tokenize(sentence)
ps = PorterStemmer()
for w in words:
	rootWord=ps.stem(w)
	print(rootWord)