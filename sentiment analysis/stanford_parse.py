# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
# Function that converts words to abstract polarity values
from polarity import polarity
# Gets the phrase of a sentence
from Tree import listify
# Functions for populating the knowledge base
from SentimentDict import read_files, read_det_file
# Function for grouping, voting and returns the sentient of a sentece
from sentence_sentiment import sentence_sentiment
# Function that splits both +ve and -ve reviews by line
from reviewParse import initDic

# populates a dictionary of words to which the sentiment is known
basal_sentiment_dictionary = {}
read_files(basal_sentiment_dictionary)

# Generates a list of known determiners
basal_determiner_bank = read_det_file()

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

reviews = initDic()

pos_reviews = reviews['positiveReviews']
neg_reviews = reviews['negativeReviews']

right = 0
total = 0
for text in neg_reviews:

    text = str(text)
    if text != '':
        print(text)
        total +=1
        # Result of said parsing : Type (json)
        output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

        #This is the tree
        s = output['sentences'][0]['parse']

        # Reformatting as an NLTK obj same type as s
        tree = Tree.fromstring(s)
        # tree.pretty_print()

        # Get the phrase from the tree
        phrases = listify(tree)

        # Converts words in phrase to abstract polarity symbols
        words_as_polarity = polarity(phrases,basal_sentiment_dictionary,basal_determiner_bank)

        # Calcualtes the sentiment of a sentence as per 'Sentiment Composition'
        sentiment = sentence_sentiment(words_as_polarity)
        try:
            if int(sentiment) > 0:
                right+=1
        except:
            pass
print((right/total) *100)
