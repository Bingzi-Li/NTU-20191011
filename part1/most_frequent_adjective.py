#!/usr/bin/env python
# coding: utf-8
# In[7]:
import numpy as np
import pandas as pd
import nltk
import math
import os.path
from nltk import FreqDist

'Get the path of the dataset'
review_path = '../data/reviewTaggingAll100.json'
os.path.exists(review_path)

'Tokenize the texts and output the json file'
review_df = pd.read_json(review_path, lines=True, encoding='latin-1')
'''review_df['tokenize'] = review_df['text'].apply(nltk.word_tokenize)
review_df['pos_tag'] = review_df['tokenize'].apply(nltk.pos_tag)
review_df.to_json(r'../data/reviewTagging100.json', orient='records', lines=True)'''

'First part: Select adjectives and find their probability in regard to their ratings'
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

'Second part: Select adjectives and find their indicativeness in regard to their ratings'
'Get the distribution of all the tokens in the dataset'
data_length = len(review_df)
data_tokens = []
for i in range(0, data_length):
    data_tokens = data_tokens +  review_df.iloc[i]['tokenize']
data_fdist = FreqDist(data_tokens)

for stars in range(1, 6):
    output = {'rating': stars, 'adjs':[]}
    for i in range(0, data_length):
        review = review_df.iloc[i]
        if  review['stars']==stars:
            tagged = review['pos_tag']
            review_adjs = [word for word, tag in tagged if tag in ('JJ')]
            output['adjs'] = output['adjs'] + review_adjs
    distinct_tokens = list(set(output['adjs']))
    adj_fdist = FreqDist(output['adjs'])

    'Generate pairs with adjectives and its indicativeness'
    output_indicativeness = []
    for adj in distinct_tokens:
        output_indicativeness.append((adj, adj_fdist.freq(adj) * math.log2(adj_fdist.freq(adj)/data_fdist.freq(adj))))
    output_indicativeness.sort(key=lambda tup: tup[1], reverse=True)
    print(output_indicativeness[0:5])





