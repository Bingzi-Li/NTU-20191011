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


review_df = pd.read_json(review_path, lines=True)
review_df.head()


# In[38]:


review_random_idx = np.array(np.random.rand(5)*len(review_df), dtype=np.int32)

review_random_df = review_df.iloc[review_random_idx]
review_random_df = review_random_df.reset_index()

review_random_df


# In[39]:


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

review_random_df['tokenize'] = review_random_df['text'].apply(nltk.word_tokenize)
review_random_df['pos_tag'] = review_random_df['tokenize'].apply(nltk.pos_tag)


# In[48]:


review_random_df.to_json(r'../data/reviewTagging100.json', orient='records', lines=True)

