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

    plt.figure()
    plt.plot(token_count_without_stem[0], token_count_without_stem[1], label='Without Stemming')
    plt.plot(token_count_with_stem[0], token_count_with_stem[1], label='With Stemming')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Number of Reviews')
    plt.legend()
    plt.savefig('With&Without_Stemming_Together.png', bbox_inches='tight', dpi=100)

    fig, axs = plt.subplots(2)
    axs[0].plot(token_count_without_stem[0], token_count_without_stem[1], label='Without Stemming')
    axs[1].plot(token_count_with_stem[0], token_count_with_stem[1], label='With Stemming')
    for ax in axs:
        ax.set(ylabel='Number of Reviews')
    axs[0].set(xlabel='Number of Tokens without Stemming')
    axs[1].set(xlabel='Number of Tokens with Stemming')
    fig.tight_layout()
    fig.savefig('With&Without_Stemming_Separate.png', bbox_inches='tight', dpi=100)


def plot_frequency_for_top_frequency_words(reviews_without_stem, reviews_with_stem):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stop_words.update(['The', 'n\'t', 'I', '\'s', 'We', 'get', 'would', 'It', 'one', 'place', 'They', 'go', 'This',
                       '\'ve', 'got', 'us', 'my', 'could', 'also', 'even', 'also', '\'m', 'always', 'came', 'come',
                       'made', 'said', 'going', 'know', 'If', 'day', '\'re', 'two', '2', 'say', 'take', 'way', 'still',
                       'ever', 'give', 'told', 'eat', 'minutes', 'around', 'So', 'asked', 'see', 'There', 'since',
                       '\'ll', 'took', 'She', 'He', 'You', 'next', 'But', '3', 'And', '5', 'When', 'every', 'A',
                       'something', 'tried', 'ca', 'Not', 'everything', '\'d', 'called', 'done', 'coming', 'things',
                       'wa', 'thi', 'veri', 'realli', 'becaus', 'alway', 'ha', 'ani', 'use', 'really' 'This',
                       'My', 'make', 'went', 'ask', 'definit', 'definitely', 'work', 'thing', 'order', 'ordered'])

    top_frequency_words_without_stem = {}
    top_frequency_words_with_stem = {}
    for i in range(len(reviews_without_stem)):
        for token in reviews_without_stem[i]:
            if token not in stop_words and not re.match(r'^[_\W]+$', token):
                if token not in top_frequency_words_without_stem:
                    top_frequency_words_without_stem[token] = 1
                else:
                    top_frequency_words_without_stem[token] += 1
        for token in reviews_with_stem[i]:
            if token not in stop_words and not re.match(r'^[_\W]+$', token):
                if token not in top_frequency_words_with_stem:
                    top_frequency_words_with_stem[token] = 1
                else:
                    top_frequency_words_with_stem[token] += 1

    top_frequency_words_with_stem = sorted(top_frequency_words_with_stem.items(), key=operator.itemgetter(1))
    top_frequency_words_without_stem = sorted(top_frequency_words_without_stem.items(), key=operator.itemgetter(1))
    top_frequency_words_with_stem = top_frequency_words_with_stem[len(top_frequency_words_with_stem) - 20
                                                                  :len(top_frequency_words_with_stem)]
    top_frequency_words_without_stem = top_frequency_words_without_stem[len(top_frequency_words_without_stem) - 20
                                                                  :len(top_frequency_words_without_stem)]
    top_frequency_words_with_stem = list(zip(*top_frequency_words_with_stem))
    top_frequency_words_without_stem = list(zip(*top_frequency_words_without_stem))

    plt.figure()
    plt.bar(range(20), top_frequency_words_without_stem[1], align='center')
    plt.xticks(range(20), top_frequency_words_without_stem[0], rotation='60')
    plt.ylabel('Number of Occurence without Stemming')
    plt.savefig('Top_Frequency_Words_Without_Stemming.png', bbox_inches='tight', dpi=100)

    plt.figure()
    plt.bar(range(20), top_frequency_words_with_stem[1], align='center')
    plt.xticks(range(20), top_frequency_words_with_stem[0], rotation='60')
    plt.ylabel('Number of Occurence with Stemming')
    plt.savefig('Top_Frequency_Words_With_Stemming.png', bbox_inches='tight', dpi=100)


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








