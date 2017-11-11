# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
from polarity import polarity
from Tree import listify, is_even, pairwise
from SentimentDict import read_files, read_det_file


# Instantiate dictionary that
# will contain {"the word": word, "the sentiment": sentiment}
basal_sentiment_dictionary = {}
read_files(basal_sentiment_dictionary)

# Instantiate dictionary that will contain [word,word,word]
basal_determiner_bank = read_det_file()

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

# Text to be parsed
text = 'the senators supporting the leader failed to praise his hopeless HIV prevention program'
# Result of said parsing : Type (json)
output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

#This is the tree
s = output['sentences'][0]['parse']

# Reformatting as an NLTK obj same type as s
tree = Tree.fromstring(s)
#tree.pretty_print()

# Get the phrase from the tree
phrases = listify(tree)

frazes = polarity(phrases,basal_sentiment_dictionary,basal_determiner_bank)

print(frazes)
