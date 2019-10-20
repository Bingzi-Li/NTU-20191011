import numpy as np
import pandas as pd
import re

import nltk
import flair

# count the number of words in each sentence
def word_count(sentences):
  count = []

  for sentence in sentences:
    count.append(len(re.findall(r'\w+', sentence)))

  return count


nltk.download('vader_lexicon')
analyzer = nltk.sentiment.vader.SentimentIntensityAnalyzer()


# define vader sentiment analysis tool
def sentiment_vader(sentences):
  value = []

  for sentence in sentences:
    value.append(analyzer.polarity_scores(sentence)['compound'])

  return value


classifier = flair.models.TextClassifier.load('en-sentiment')


# define flair sentiment analysis tool
def sentiment_flair(sentences):
    value = []

    for sentence in sentences:
        flair_sentence = flair.data.Sentence(sentence)
        classifier.predict(flair_sentence)

        labels = str(flair_sentence.labels[0]).split()
        value.append((-1 if labels[0]=='NEGATIVE' else 1)*float(labels[1][1:7]))

    return value

# define the weighted score function for calculating weighted average
def weighted_score(segmented):
    weighted_score = []

    for i in range(len(segmented)):

        count, score = segmented.iloc[i][0], segmented.iloc[i][1]
        total_count, total_score = 0, 0

        for j in range(len(count)):
            total_count += count[j]
            total_score += count[j]*score[j]

        if(total_count!=0):
            weighted_score.append(total_score/total_count)
        else:
            weighted_score.append(0)

    return weighted_score


# conclude if the expression is negative based on the weighted score
def negex(weighted_score):

    if weighted_score<0:
        return "NEGATIVE"
    else:
        return "POSITIVE"



review_gh_url = '../data/reviewSamples20.json'
review_df = pd.read_json(review_gh_url, lines=True).loc[:,['review_id', 'business_id', 'user_id', 'stars', 'text', 'date']]

review_df['sentences'] = review_df['text'].apply(nltk.sent_tokenize)
review_df['word_count']=review_df['sentences'].apply(word_count)

review_df['score_vader']=review_df['sentences'].apply(sentiment_vader)
review_df['weighted_vader']=weighted_score(review_df[['word_count', 'score_vader']])
review_df['negex_vader']=review_df['weighted_vader'].apply(negex)

review_df['score_flair']=review_df['sentences'].apply(sentiment_flair)
review_df['weighted_flair']=weighted_score(review_df[['word_count', 'score_flair']])
review_df['negex_flair']=review_df['weighted_flair'].apply(negex)

review_df.to_json('../output/reviewSentiment20.json')
review_df.to_excel('../output/reviewSentiment20.xlsx')
