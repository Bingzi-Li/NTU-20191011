import spacy
import pandas as pd
nlp = spacy.load('en')

#adj_doc = nlp("The company's customer service was terrible.")

arr = ["The customer service is good", "Give me some good food", "The restaurant's food is very good", "The food in this restaurant is surprisingly good"]

tuple_list = []

def get_subj_pairs(doc, verbose=False):
    """Return tuples of (multi-noun word, adjective) for document."""
    compounds = [tok for tok in doc if tok.pos_ == 'NOUN' or tok.pos_ == 'PROPN'] # Get list of compounds in doc
    if compounds:
        for tok in compounds:
            pair_item_1, pair_item_2 = (False, False) # initialize false variables
            noun = doc[tok.i: tok.head.i+1]
            pair_item_1 = noun
            # If noun is in the subject, we may be looking for adjective in predicate
            # In simple cases, this would mean that the noun shares a head with the adjective
            if noun.root.dep_ == 'nsubj':
                sub_adj_list = [r for r in noun.root.head.rights if r.pos_ == 'ADJ']
                if sub_adj_list:
                    pair_item_2 = sub_adj_list[0]
                if verbose == True: # For trying different dependency tree parsing rules
                    print("Noun: ", noun)
                    print("Noun root: ", noun.root)
                    print("Noun root head: ", noun.root.head)
                    print("Noun root head rights: ", [r for r in noun.root.head.rights if r.pos_ == 'ADJ'])
            if pair_item_1 and pair_item_2:
                tuple_list.append((pair_item_1, pair_item_2))
    return

def get_obj_pairs(doc, verbose=False):
    """Return tuples of (multi-noun word, adjective) for document."""
    compounds = [tok for tok in doc if tok.pos_ == 'NOUN' or tok.pos_ == 'PROPN']  # Get list of compounds in doc
    if compounds:
        for tok in compounds:
            pair_item_1, pair_item_2 = (False, False)  # initialize false variables
            pair_item_1 = tok
            # If noun is in the direct or inderect object, we may be looking for adjective in front
            # In simple cases, this would mean that the object is decorated by the adjective
            if tok.dep_ == 'dobj' or tok.dep_ == 'iobj':
                obj_adj_list = [r for r in tok.lefts if r.pos_ == 'ADJ']
                if obj_adj_list:
                    pair_item_2 = obj_adj_list[0]
                if verbose == True:  # For trying different dependency tree parsing rules
                    print("Noun: ", tok)
                    print("Noun root head: ", tok.head)
                    print("Noun root head lefts: ", [r for r in tok.lefts if r.pos_ == 'ADJ'])
                    print(pair_item_1, pair_item_2)
            if pair_item_1 and pair_item_2:
                tuple_list.append((pair_item_1, pair_item_2))
    return

for k in range(0, 4):
    adj_doc = nlp(arr[k])
    get_subj_pairs(adj_doc)
    get_obj_pairs(adj_doc)

print(tuple_list)
