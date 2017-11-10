# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
# Takes an nltk tree and flattens it to an array of NP & VPs
from Tree import listify
# Takes an annotated array and returns True if that list is even
from Tree import is_even
# Pairs list elements
from Tree import pairwise
# Generates a dictionary of abstract word sentiment using corpora extraction
from SentimentDict import read_files
from SentimentDict import read_det_file

# Instantiate dictionary that
# will contain {"the word": word, "the sentiment": sentiment}
basal_sentiment_dictionary = {}

# Instantiate dictionary that will contain [word,word,word]
basal_determiner_bank = read_det_file()

# Populate dictionary {"the word": word, "the sentiment": sentiment} with words
# from Corpora
read_files(basal_sentiment_dictionary)

print(basal_determiner_bank)

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

# Text to be parsed
text = 'The is a nokia phone review'
# Result of said parsing : Type (json)
output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

#This is the tree
s = output['sentences'][0]['parse']

# Reformatting as an NLTK obj same type as s
tree = Tree.fromstring(s)
#tree.pretty_print()

# Get the phrase from the tree
phrases = listify(tree)


for phrase in phrases:
    # if is_even(phrase)
    for i in range(1,len(phrase),2):
        if (i+1 == len(phrase)):
            print([phrase[i]])
        elif (len([phrase[i],phrase[i+1]]) == 2):
            if phrase[i] in basal_sentiment_dictionary:
                print(basal_sentiment_dictionary[phrase[i]])
            elif phrase[i] in basal_determiner_bank:
                print('DET')
            else:
                print('N')
            if phrase[i+1] in basal_sentiment_dictionary:
                print(basal_sentiment_dictionary[phrase[i+1]])
            elif phrase[i+1] in basal_determiner_bank:
                print('DET')
            else:
                print('N')
            #sentiment1 = basal_sentiment_dictionary.keys([phrase[i]])
            #sentiment2 = basal_sentiment_dictionary.keys([phrase[i+1]])
            print([phrase[i],phrase[i+1]])
