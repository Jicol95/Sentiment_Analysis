# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
from nltk import Tree


def stanford_parse(text):
    #  Start StanfordCoreNLP server at port 9000
    stanford = StanfordCoreNLP('http://localhost:9000')

    # Result of said parsing : Type (json)
    output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

    #This is the tree
    s = output['sentences'][0]['parse']

    # Reformatting as an NLTK obj same type as s
    tree = Tree.fromstring(s)
    #tree.pretty_print()
    return tree
