import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import re
import os
import pandas as pd

review_path = '../data/reviewTaggingAll100.json'
os.path.exists(review_path)

'Tokenize the texts and output the json file'
review_df = pd.read_json(review_path, lines=True, encoding='latin-1')

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