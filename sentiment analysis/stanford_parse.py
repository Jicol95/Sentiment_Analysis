# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Import regular expression
import re
# Functions for populating the knowledge base
from SentimentDict import read_files, read_det_file, read_negate_file
# returns a dict of reviews
from reviewParse import initDic
from classify import classify

# populates a dictionary of words to which the sentiment is known
basal_sentiment_dictionary = {}
read_files(basal_sentiment_dictionary)

# Generates a list of known determiners
basal_determiner_bank = read_det_file()

# Generates a list of known negators
negators_bank = read_negate_file()


# dictionary of reviews
reviews = initDic()
posReviews = reviews['positiveReviews']
negReviews = reviews['negativeReviews']

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

# # Text to be parsed
# text = "The senotors supporting the leader failed to support his hopeless HIV prevention program."

counter = 0
right = 0
neutral_count = 0
for text in negReviews:
    if text != '':
        counter += 1
        words = str(text)
        sent = classify(words, basal_sentiment_dictionary, basal_determiner_bank, negators_bank, stanford)
        if int(sent) < 0:
            right +=1
        if int(sent) == 0:
            neutral_count += 1
        print('\n\n\n\n')

neg_precision = 'Negative precision: ' + str((right/counter) *100)
neg_neutral_prescion = 'Negative precision (excluding neutral): ' + str((right/(counter - neutral_count))*100)

counter = 0
right = 0
neutral_count = 0
for text in posReviews:
    if text != '':
        counter += 1
        words = str(text)
        sent = classify(words, basal_sentiment_dictionary, basal_determiner_bank, negators_bank, stanford)
        if int(sent) > 0:
            right +=1
        if int(sent) == 0:
            neutral_count += 1
        print('\n\n\n\n')

pos_precision = 'Positive precision: ' + str((right/counter) *100)
pos_neutral_prescion = 'Positive precision (excluding neutral): ' + str((right/(counter - neutral_count))*100)

print(neg_precision)
print(neg_neutral_prescion)
print(pos_precision)
print(pos_neutral_prescion)
