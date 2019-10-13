import numpy as np
import pandas as pd

import nltk

import os.path

review_path = 'data/reviewSelected100.json'
os.path.exists(review_path)

review_df = pd.read_json(review_path, lines=True)
review_df.head()

review_df_groupby_bid = review_df.groupby('business_id')

review_bid_list = []
review_bid_dict = {}

for bid, bid_df in review_df_groupby_bid:
    review_bid_list.append(bid)
    review_bid_dict[bid]=bid_df.reset_index()
