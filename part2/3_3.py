import pandas as pd
import spacy
import os.path

review_path = '../data/reviewSelected100.json'
os.path.exists(review_path)

# Get the reviews text, stores in array
review_df = pd.read_json(review_path, lines=True)
review_df.head()
# Group data by business_id
review_df_groupby_bid = review_df.groupby('business_id')

review_bid_list = []
review_bid_dict = {}

for bid, bid_df in review_df_groupby_bid:
    review_bid_list.append(bid)
    review_bid_dict[bid] = bid_df.reset_index()

# Get the reviews text of certain business_id, stores in array
review_bid_text = []
for i in range(100):
    review_bid_text.append(review_bid_dict['1Fpk8ibHhZYnCw8fnGny8w']['text'][i])

arr = review_bid_text

print(review_bid_text)

#print(review_bid_list[27]) # 4 14 18 19 27

# arr = ["The food is good", "Give me some good food", "The restaurant's food is very good", "The food in this restaurant is surprisingly good"]

nlp = spacy.load('en')

# Create a dictionary with Key:Value pair - (Noun, Adjective):count
countdict={}

# k loop traverse the array of reviews
for k in range(0, 10):
    doc = nlp(arr[k])

    # i loop traverse to find all the Noun, Adjective pairs
    for i, token in enumerate(doc):
        if token.pos_ not in ('NOUN', 'PROPN'):
            continue

        # j loop to update the dictionary, by adding unseen pairs and increment count of seen pairs
        for j in range(i + 1, len(doc)):
            if doc[j].pos_ == 'ADJ':
                key = (str(token), str(doc[j]))
                # print(countdict.keys())
                if key in countdict.keys():
                    countdict[key] = countdict[key]+1
                else:
                    countdict[key] = 1
                break

# print the (Noun, Adjective) with its count in a sorted order
a1_sorted_keys = sorted(countdict, key=countdict.get, reverse=True)
for r in a1_sorted_keys:
    print(r, countdict[r])

