# NLP-comments
Third party libraries (install via python pip):

nltk ==3.4.5

spacy == 2.2.1

pandas == 0.25.1

numpy == 1.17.2

ndjson == 0.2.0

matplotlab == 3.1.1

The source code python scripts can be found in the directory data_analysis, pair_summarizer, and application. The scripts are independent and the explanation of the scripts are given below:

3. tokenization_stemming.py

   ​	Running the script will generate 4 png files, include 2 plots for number of reviews of the specific length against the length of the review in terms of tokens, and 2 histograms for top 20 frequent words.

5. most_frequent_adjective.py

   ​	Running the script will output the most frequent adjectives (in the form of (word, frequency count)) and the most indicative adjectives (in the form of (word, “indicativeness”)) in respect to the stars the reviews has.

6. application: sentiment_analysis.py. 

To scripts can be run in any IDE (preferably pycharm)

The sample output are in the directory “output”, and their meanings are explained below:

1. revireSegemented100.json
2. reviewSentiment20.json
3. reviewTagging100.json
4. reviewTaggingRandom5.json
5. reviewTaggingSelect5.json
6. reviewTokenized100.json: This json file contains all the stemmed and unstemmed tokens extracted from the reviews.
 