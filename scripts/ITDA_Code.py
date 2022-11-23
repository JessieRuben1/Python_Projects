# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:40:12 2020

@author: admin
"""

import pandas as pd
import numpy
import csv
import nltk
from nltk.tokenize import word_tokenize
import os
import re




#function to display number of rows, columns and the label class
def display_order():
    columns, rows = train_file.shape
    print("The number of rows is " + str(rows))
    print("The number of columns is " + str(columns))
    print(train_file['label'])
    

  #function to remove punctuation  
def remove_punc(name):
    result = ''
    with open('name','r') as rem:
        reader = csv.reader(rem)
        for row in reader:
            row = re.sub('[^A-Za-z0-9]+', '', str(row))
            result += row + ','
    return result
            


#Read the train.csv file and test.csv file
train_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\train.csv")
test_file = pd.read_csv(r"C:\Users\admin\Documents\2020 honours\ITDA411 assignment\test.csv")
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'train_file')

#display number of rows and columns and label class

print(display_order())

#tokenization on test.csv and train.csv


# with open ('train_file', 'r') as tr_file:
#     reader = csv.DictReader(tr_file)
#     for train in reader:
#         tweet = train['tweet']
#         print('Tweet: %s' % tweet)
#         tokens = word_tokenize(tweet)
#         print(tokens)


# with open('text_file', 'r') as te_file:
#     reader = csv.DictReader(te_file)
#     for test in reader:
#         tweett = test['tweet']
#         print('Tweet: %s' % tweett)
#         tokenss = word_tokenize(tweett)
#         print(tokenss)
        
#remove punctuation

print(remove_punc(train_file).lower())
print(remove_punc(test_file).lower())

#stop word removal

