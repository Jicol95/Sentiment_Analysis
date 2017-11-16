# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
# Function that converts words to abstract polarity values
from polarity import polarity
# Gets the phrase of a sentence
from Tree import listify
from sentence_sentiment import sentence_sentiment

def classify(text, basal_sentiment_dictionary, basal_determiner_bank, negators_bank, stanford):

    words = str(text)
    # Result of said parsing : Type (json)
    output = stanford.annotate(words, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

    #This is the tree
    s = output['sentences'][0]['parse']

    # Reformatting as an NLTK obj same type as s
    tree = Tree.fromstring(s)
    # tree.pretty_print()

    # Get the phrase from the tree
    phrases = listify(tree, basal_sentiment_dictionary, negators_bank)

    # Converts words in phrase to abstract polarity symbols
    words_as_polarity = polarity(phrases,basal_sentiment_dictionary,basal_determiner_bank)

    # Calcualtes the sentiment of a sentence as per 'Sentiment Composition'
    sentiment = sentence_sentiment(words_as_polarity)
    return sentiment
    s = ''
    output = ''
