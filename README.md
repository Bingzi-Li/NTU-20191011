# NTU-20191011
## NTU CZ4045 Natural Language Processing Assignment
### Authors: Li Bingzi, Li Guanlong, Wu Ziang, Yong Hao & Zhang Yuehan

Third party libraries (install via python pip):

nltk ==3.4.5

spacy == 2.2.1

pandas == 0.25.1

numpy == 1.17.2

ndjson == 0.2.0

matplotlab == 3.1.1

flair == 0.4.3

The source code python scripts can be found in the directory data_analysis, pair_summarizer, and application. The scripts are independent and the explanation of the scripts are given below:

1. data_analysis/sentence_segmentation.py
    Running this script will first perform sentence segmentation on reviews with output being exported file and second plot the distribution of the data for particular rating star (i.e., 1 to 5).

2. data_analysis/tokenization_stemming.py

    ​Running the script will generate 4 png files, include 2 plots for number of reviews of the specific length against the length of the review in terms of tokens, and 2 histograms for top 20 frequent words.

3. data_analysis/pos_tagging.py

    Running this script will randomly select five reviews and perform POS tagging on the text.

4. data_analysis/most_frequent_adjective.py

    Running the script will output the most frequent adjectives (in the form of (word, frequency count)) and the most indicative adjectives (in the form of (word, indicativeness)) in respect to the stars the reviews has.

5. pair_summarizer/noun_adjective.py

    Running this script will output the <Noun-Adjective> pairs extracted from reviews of 5 randomly selected business, 100 reviews each. Each pair has a count to denote the frequency.

6. application/sentiment_analysis.py.

    Running this script will output the spreadsheet containing the sentiment analysis result of review text using both Vader and Flair.

The sample output are in the directory output and are explained below:

1. output/reviewSegmented100.json

    This file is output from data_analysis/sentence_segmentation.py. It replaces the text of original data file with a list of segmented sentences, and add another attribute sentence length.

2. output/reviewTagging5.json

    This file is output from data_analysis/pos_tagging.py. It performs the POS tagging on tokens after tokenization and saves the result in a new column.

3. output/reviewSentiment20.*

    This file is output from application/sentiment_analysis.py. It contains the sentiment analysis result on each individual sentence, using both Vader and Flair tools, weighted score of positive and negative ranging from 1 to -1.
