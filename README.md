# NLP-comments
Third party libraries (install via python pip):

nltk ==3.4.5

spacy == 2.2.1

pandas == 0.25.1

numpy == 1.17.2

ndjson == 0.2.0

matplotlab == 3.1.1

flair == 0.4.3

The source code python scripts can be found in the directory data_analysis, pair_summarizer, and application. The scripts are independent and the explanation of the scripts are given below:

1. sentence_segmentation.py
...The script contains two methods:
```python
def get_segmented_reviews(retrievepath, savepath):
    '''This method takes in retrieve path to get the data source json file and dump the data into other file in save path, after doing sentence segmentation on reviews.'''
def plot(retrievepath, rating):
'''This method shows the distribution of the data for particular rating star (i.e., 1 to 5). In each plot, the x-axis is the length of a review in number of sentences, and the y-axis is the number of reviews of such length. '''
```
3. tokenization_stemming.py
   ​	Running the script will generate 4 png files, include 2 plots for number of reviews of the specific length against the length of the review in terms of tokens, and 2 histograms for top 20 frequent words.

5. most_frequent_adjective.py

   Running the script will output the most frequent adjectives (in the form of (word, frequency count)) and the most indicative adjectives (in the form of (word, “indicativeness”)) in respect to the stars the reviews has.

6. <Noun-Adjective> Summarizer: noun_adjective.py

   Running this script will output the <Noun-Adjective> pairs extracted from reviews of 5 randomly selected business, 100 reviews each. Each pair has a count to denote the frequency. 

7. application: sentiment_analysis.py. 

To scripts can be run in any IDE (preferably pycharm)

The sample output are in the directory “output”, and their meanings are explained below:

1. revireSegemented100
... This file is the result of running get_segmented_reviews(retrievepath, savepath) in sentence_segmentation.py.It replaces the text ...in original data file with a list if segmented sentences, and add another atribute sentence length.

2. reviewSentiment20
3. reviewTagging100
4. reviewTaggingRandom5
5. reviewTaggingSelect5
6. reviewTokenized100