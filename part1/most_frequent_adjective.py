#!/usr/bin/env python
# coding: utf-8
# In[7]:
import numpy as np
import pandas as pd
import nltk
import os.path
from nltk import FreqDist

'''Get the path of the dataset'''
review_path = '../data/reviewTaggingAll100.json'
os.path.exists(review_path)

'''Tokenize the texts and output the json file'''
review_df = pd.read_json(review_path, lines=True, encoding='latin-1')
'''review_df['tokenize'] = review_df['text'].apply(nltk.word_tokenize)
review_df['pos_tag'] = review_df['tokenize'].apply(nltk.pos_tag)
review_df.to_json(r'../data/reviewTagging100.json', orient='records', lines=True)'''

'''First part: Select adjectives and find their probability in regard to their ratings'''
'''data_length = len(review_df)
for stars in range(1, 6):
    output = {'rating': stars, 'adjs':[]}
    for i in range(0, data_length):
        review = review_df.iloc[i]
        if  review['stars']==stars:
            tagged = review['pos_tag']
            review_adjs = [word for word, tag in tagged if tag in ('JJ')]
            output['adjs'] = output['adjs'] + review_adjs
    adj_fdist = FreqDist(output['adjs'])
    print(adj_fdist.most_common(5))'''

'''First part: Select adjectives and find their probability in regard to their ratings'''
data_length = len(review_df)
for stars in range(1, 6):
    output = {'rating': stars, 'adjs':[]}
    for i in range(0, data_length):
        review = review_df.iloc[i]
        if  review['stars']==stars:
            tagged = review['pos_tag']
            review_adjs = [word for word, tag in tagged if tag in ('JJ')]
            output['adjs'] = output['adjs'] + review_adjs
    adj_fdist = FreqDist(output['adjs'])
    print(adj_fdist.most_common(5))