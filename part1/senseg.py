from nltk import sent_tokenize
import matplotlib.pyplot as plt
import numpy as np
import ndjson

# current retrievepath = '../data/reviewSelected100.json'
# current get_segmented_reviews savepath and plot retrievepath = '../data/reviewSegmented100.json'


def get_segmented_reviews(retrievepath, savepath):
    '''This method takes in rtrieve path to get the data source json file and dump the data into other file in save path, after doing sentence segmentation on reviews.'''
    
    # open the json file and read the reviews in. 
    # The file is actually ndjson(seperated by newlines not commas)
    try:
        with open(retrievepath, encoding = 'latin-1') as f:
            datastore = ndjson.load(f)
    except IOError:
        print('An error occurred trying to read the file.')

    # using sent_tokenize() to split a review text into a list of sentences.
    for review in datastore:
        review['text'] = sent_tokenize(review['text'])
        # number of sentence in each review text
        review['num_sentence'] = len(review['text'])

    # save the sengmented comments to data folder for further analysis
    try: 
        with open(savepath, 'w+') as f:
            ndjson.dump(datastore, f)
    except IOError:
        print('An error occurred trying to save the file.')


def plot(retrievepath, rating):

    '''This method shows the distribution of the data for particular rating star (i.e., 1 to 5). In each plot, the x-axis is the length of a review in number of sentences, and the y-axis is the number of reviews of such length. '''
    
    # initialising list of dictionary used to record [{length:num of reviews}]
    plot_data = {}
    
    # open the json file and read the reviews in. 
    # The file is actually ndjson(seperated by newlines not commas)
    try:
        with open(retrievepath, encoding = 'latin-1') as f:
            datastore = ndjson.load(f)
    except IOError:
        print('An error occurred trying to read the file.')
    
    # get number of comments for each (ratings, length) pair
    for review in datastore:
        if rating == int(review['stars']):
            key = str(review['num_sentence'])
            if key in plot_data.keys():
                plot_data[key] += 1
            else:
                plot_data[key] = 1

    # prepare x and y data
    # list returned by .keys() method is not sorted
    groups = sorted([int(key) for key in plot_data.keys()])
    values = [plot_data[str(i)] for i in groups]
    
    # chart formatting 
    y_pos = np.arange(len(groups))
    # plot bar chart
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, groups)
    plt.ylabel('review length(in num of sentences)')
    plt.title('Segmentation Analysis of Rating '+str(rating))
    plt.show()

        