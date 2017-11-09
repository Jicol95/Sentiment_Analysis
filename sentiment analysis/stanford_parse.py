# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
# Install: pip install nltk
from pycorenlp import StanfordCoreNLP
from nltk.tree import Tree
from SentimentDict import readFiles

# Instantiate dictionary that
# will contain {"the word": word, "the sentiment": sentiment}

sentimentDictionary = {}

# Populate dictionary {"the word": word, "the sentiment": sentiment} with words
# from Corpora
readFiles(sentimentDictionary)

# Test for the sentimentDictionary
# print(sentimentDictionary['failed'])

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

# Text to be parsed
text = '''The senators supporting the leader failed to praise his hopeless HIV prevention program'''

# Result of said parsing : Type (json)
output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

#This is the tree
s = output['sentences'][0]['parse']

# Reformatting as an NLTK obj same type as s
tree = Tree.fromstring(s)
# tree.pretty_print()

for leaf in tree.subtrees():
    leaf.pretty_print()
