# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:01:40 2020

@author: admin
"""

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict

import pandas as pd
import numpy
import csv
import nltk
from nltk.tokenize import word_tokenize
import os
import re

train_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\train.csv")
test_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\test.csv")

tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

sentence=str(train_file[['tweet']])
tokens = word_tokenize(sentence)
lemma_function = WordNetLemmatizer()
for token, tag in pos_tag(tokens):
	lemma = lemma_function.lemmatize(token, tag_map[tag[0]])
	print(token, "=>", lemma)