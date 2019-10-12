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
from nltk import FreqDist

review_path = '../data/reviewTaggingAll100.json'
os.path.exists(review_path)

'Tokenize the texts and output the json file'
review_df = pd.read_json(review_path, lines=True, encoding='latin-1')

"Group review by bid"
review_df_groupby_bid = review_df.groupby('business_id')
review_bid_list = []
review_bid_dict = {}

for bid, bid_df in review_df_groupby_bid:
    review_bid_list.append(bid)
    review_bid_dict[bid]=bid_df.reset_index()


'First part: Select adjectives and find their probability in regard to their ratings'
data_length = len(review_df)
output = []
for i in range(0, data_length):
    tagged =  review_df.iloc[i]['pos_tag']
    review_adjs = [word for word, tag in tagged if tag in ('JJ')]
    output = output + review_adjs

print(output)
