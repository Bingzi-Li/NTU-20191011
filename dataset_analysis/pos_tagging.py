import numpy as np
import pandas as pd

import nltk

import os.path


review_path = '../data/reviewSelected100.json'
os.path.exists(review_path)

review_df = pd.read_json(review_path, lines=True)
review_df.head()

'Generate five random indexes'
review_random_idx = np.array(np.random.rand(5)*len(review_df), dtype=np.int32)

review_random_df = review_df.iloc[review_random_idx]
review_random_df = review_random_df.reset_index()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

'Tokenize the text and Tag the Part-Of-Speech of each words'
review_random_df['tokenize'] = review_random_df['text'].apply(nltk.word_tokenize)
review_random_df['pos_tag'] = review_random_df['tokenize'].apply(nltk.pos_tag)

'Output the resulting json '
review_random_df.to_json(r'../output/reviewTagging5.json', orient='records', lines=True)
