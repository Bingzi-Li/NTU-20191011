#!/usr/bin/env python
# coding: utf-8
# In[7]:
import numpy as np
import pandas as pd
import nltk
import os.path

# In[2]:
review_path = '../data/reviewSelected100.json'
os.path.exists(review_path)
# In[3]:
review_df = pd.read_json(review_path, lines=True, encoding='latin-1')
review_df.head()
review_df['tokenize'] = review_df['text'].apply(nltk.word_tokenize)
review_df['pos_tag'] = review_df['tokenize'].apply(nltk.pos_tag)
# In[48]:
review_df.to_json(r'../data/reviewTagging100.json', orient='records', lines=True)

