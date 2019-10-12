import nltk
import matplotlib.pyplot as plt
import collections
import ndjson
import re
nltk.download('punkt')


def get_reviews(path):
    try:
        with open(path) as f:
            data_set = ndjson.load(f)
    except IOError:
        print('An error occurred trying to read the file.')
    all_reviews = []
    for data in data_set:
        all_reviews.append(data['text'])
    return all_reviews


def save_data(data, path):
    try:
        with open(path, 'w+') as f:
            ndjson.dump(data, f)
    except IOError:
        print('An error occurred trying to save the file.')


def plot_frequency_for_num_of_tokens(reviews_without_stem, reviews_with_stem):
    token_count_without_stem = {}
    token_count_with_stem = {}
    for i in range(len(reviews_without_stem)):
        num_of_tokens_without_stem = len(set(reviews_without_stem[i]))
        num_of_tokens_with_stem = len(set(reviews_with_stem[i]))
        if num_of_tokens_without_stem not in token_count_without_stem:
            token_count_without_stem[num_of_tokens_without_stem] = 1
        else:
            token_count_without_stem[num_of_tokens_without_stem] += 1
        if num_of_tokens_with_stem not in token_count_with_stem:
            token_count_with_stem[num_of_tokens_with_stem] = 1
        else:
            token_count_with_stem[num_of_tokens_with_stem] += 1
    token_count_without_stem = sorted(token_count_without_stem.items())
    token_count_without_stem = list(zip(*token_count_without_stem))
    token_count_with_stem = sorted(token_count_with_stem.items())
    token_count_with_stem = list(zip(*token_count_with_stem))
    print(token_count_without_stem)
    print(token_count_with_stem)

    plt.figure()
    plt.plot(token_count_without_stem[0], token_count_without_stem[1], label='Without Stemming')
    plt.plot(token_count_with_stem[0], token_count_with_stem[1], label='With Stemming')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Number of Reviews')
    plt.legend()
    plt.savefig('With&Without_Stemming_Together.png', bbox_inches='tight', dpi=100)

    fig, axs = plt.subplots(2)
    axs[0].plot(token_count_without_stem[0], token_count_without_stem[1])
    axs[1].plot(token_count_with_stem[0], token_count_with_stem[1])
    for ax in axs:
        ax.set(xlabel='Number of Tokens', ylabel='Number of Reviews')
    fig.tight_layout()
    fig.savefig('With&Without_Stemming_Separate.png', bbox_inches='tight', dpi=100)


reviews = get_reviews('../data/reviewSelected100.json')
tokenized_reviews = []

for review in reviews:
    tokens = nltk.tokenize.word_tokenize(review)
    tokenized_reviews.append(list(tokens))

ps = nltk.PorterStemmer()

stemmed_reviews = []
for tokenized_review in tokenized_reviews:
    stemmed_review = []
    for token in tokenized_review:
        stem = ps.stem(token)
        stemmed_review.append(stem)
    stemmed_reviews.append(stemmed_review)

plot_frequency_for_num_of_tokens(tokenized_reviews, stemmed_reviews)



# # only for saving the tokenized data
# data_to_save = []
# for i in range(len(tokenized_reviews)):
#     review_to_save = {'tokens without stemming': tokenized_reviews[i],
#                       'tokens with stemming': stemmed_reviews[i]}
#     data_to_save.append(review_to_save)
# save_data(data_to_save, '../data/reviewTokenized100.json')

# print(len(stemmed_reviews))
# for i in range(4):
#     print(tokenized_reviews[i])
#     print(len(tokenized_reviews[i]))
#     print(len(set(tokenized_reviews[i])))
#     print(stemmed_reviews[i])
#     print(len(stemmed_reviews[i]))
#     print(len(set(stemmed_reviews[i])))







