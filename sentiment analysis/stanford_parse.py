# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
# Takes an nltk tree and flattens it to an array of NP & VPs
from Tree import listify
# Takes an annotated array and returns True if that list is even
from Tree import is_even
# Generates a dictionary of abstract word sentiment using corpora extraction
from SentimentDict import read_files

# Instantiate dictionary that
# will contain {"the word": word, "the sentiment": sentiment}
basal_sentiment_dictionary = {}

# Populate dictionary {"the word": word, "the sentiment": sentiment} with words
# from Corpora
read_files(basal_sentiment_dictionary)

#  Start StanfordCoreNLP server at port 9000
stanford = StanfordCoreNLP('http://localhost:9000')

# Text to be parsed
text = '''after several years of torture in the hands of at&t customer service i am delighted to drop them , and look forward to august 2004 when i will convert our other 3 family-phones from at&t to t-mobile !
the day finally arrived when i was sure i 'd leave sprint .
after years with that carrier 's expensive plans and horrible customer service , portability seemed heaven-sent . '''

# Result of said parsing : Type (json)
output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

#This is the tree
s = output['sentences'][0]['parse']

# Reformatting as an NLTK obj same type as s
tree = Tree.fromstring(s)
#tree.pretty_print()

phrases = listify(tree)

for phrase in phrases:
    if is_even(phrases[1]):
        pass
    elif not is_even(phase):
        pass
