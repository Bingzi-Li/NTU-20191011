import nltk
import matplotlib.pyplot as plt
import ndjson
import operator
import re

nltk.download('punkt')
nltk.download('stopwords')


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

# plot the distributions of the number of tokens given by tokenization and stemming
def plot_frequency_for_num_of_tokens(reviews_before_stem, reviews_after_stem):
    token_count_before_stem = {}
    token_count_after_stem = {}
    # count the number of reviews for each review length
    for i in range(len(reviews_before_stem)):
        num_of_tokens_before_stem = len(set(reviews_before_stem[i]))
        num_of_tokens_after_stem = len(set(reviews_after_stem[i]))
        if num_of_tokens_before_stem not in token_count_before_stem:
            token_count_before_stem[num_of_tokens_before_stem] = 1
        else:
            token_count_before_stem[num_of_tokens_before_stem] += 1
        if num_of_tokens_after_stem not in token_count_after_stem:
            token_count_after_stem[num_of_tokens_after_stem] = 1
        else:
            token_count_after_stem[num_of_tokens_after_stem] += 1
    token_count_before_stem = sorted(token_count_before_stem.items())
    token_count_before_stem = list(zip(*token_count_before_stem))
    token_count_after_stem = sorted(token_count_after_stem.items())
    token_count_after_stem = list(zip(*token_count_after_stem))

    plt.figure()
    plt.plot(token_count_before_stem[0], token_count_before_stem[1], label='Before Stemming')
    plt.plot(token_count_after_stem[0], token_count_after_stem[1], label='After Stemming')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Number of Reviews')
    plt.legend()
    plt.savefig('../figure/token_stem_combined', bbox_inches='tight', dpi=100)

    fig, axs = plt.subplots(2)
    axs[0].plot(token_count_before_stem[0], token_count_before_stem[1], label='Before Stemming')
    axs[1].plot(token_count_after_stem[0], token_count_after_stem[1], label='After Stemming')
    for ax in axs:
        ax.set(ylabel='Number of Reviews')
    axs[0].set(xlabel='Number of Tokens before Stemming')
    axs[1].set(xlabel='Number of Tokens after Stemming')
    fig.tight_layout()
    fig.savefig('../figure/token_stem_separate.png', bbox_inches='tight', dpi=100)

# plot the top-20 most frequent words, excluding the stop words, before and after stemming
def plot_frequency_for_top_frequency_words(reviews_before_stem, reviews_after_stem):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stop_words.update(['The', 'n\'t', 'I', '\'s', 'We', 'get', 'would', 'It', 'one', 'place', 'They', 'go', 'This',
                       '\'ve', 'got', 'us', 'my', 'could', 'also', 'even', '\'m', 'always', 'came', 'come', 'still',
                       'made', 'said', 'going', 'know', 'If', 'day', '\'re', 'two', '2', 'say', 'take', 'way',
                       'ever', 'give', 'told', 'eat', 'minutes', 'around', 'So', 'asked', 'see', 'There', 'since',
                       '\'ll', 'took', 'She', 'He', 'You', 'next', 'But', '3', 'And', '5', 'When', 'every', 'A',
                       'something', 'tried', 'ca', 'Not', 'everything', '\'d', 'called', 'done', 'coming', 'things',
                       'wa', 'thi', 'veri', 'realli', 'becaus', 'alway', 'ha', 'ani', 'use', 'really' 'This',
                       'My', 'make', 'went', 'ask', 'definit', 'definitely', 'work', 'thing'])

    top_frequency_words_before_stem = {}
    top_frequency_words_after_stem = {}
    # count the number of occurrence for each words
    for i in range(len(reviews_before_stem)):
        for token in reviews_before_stem[i]:
            if token not in stop_words and not re.match(r'^[_\W]+$', token):
                if token not in top_frequency_words_before_stem:
                    top_frequency_words_before_stem[token] = 1
                else:
                    top_frequency_words_before_stem[token] += 1
        for token in reviews_after_stem[i]:
            if token not in stop_words and not re.match(r'^[_\W]+$', token):
                if token not in top_frequency_words_after_stem:
                    top_frequency_words_after_stem[token] = 1
                else:
                    top_frequency_words_after_stem[token] += 1

    # select the top 20 frequent words
    top_frequency_words_after_stem = sorted(top_frequency_words_after_stem.items(), key=operator.itemgetter(1))
    top_frequency_words_before_stem = sorted(top_frequency_words_before_stem.items(), key=operator.itemgetter(1))
    top_frequency_words_after_stem = top_frequency_words_after_stem[len(top_frequency_words_after_stem) - 20
                                                                  :len(top_frequency_words_after_stem)]
    top_frequency_words_before_stem = top_frequency_words_before_stem[len(top_frequency_words_before_stem) - 20
                                                                  :len(top_frequency_words_before_stem)]
    top_frequency_words_after_stem = list(zip(*top_frequency_words_after_stem))
    top_frequency_words_before_stem = list(zip(*top_frequency_words_before_stem))

    plt.figure()
    plt.bar(range(20), top_frequency_words_before_stem[1], align='center')
    plt.xticks(range(20), top_frequency_words_before_stem[0], rotation='60')
    plt.ylabel('Number of Occurence before Stemming')
    plt.savefig('../figure/frequent_token.png', bbox_inches='tight', dpi=100)

    plt.figure()
    plt.bar(range(20), top_frequency_words_after_stem[1], align='center')
    plt.xticks(range(20), top_frequency_words_after_stem[0], rotation='60')
    plt.ylabel('Number of Occurence after Stemming')
    plt.savefig('../figure/frequent_stem.png', bbox_inches='tight', dpi=100)


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
plot_frequency_for_top_frequency_words(tokenized_reviews, stemmed_reviews)
