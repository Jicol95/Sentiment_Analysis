# Install: pip install pycorenlp && wget http://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip
from pycorenlp import StanfordCoreNLP
# Install: pip install nltk
from nltk.tree import Tree
from textblob import TextBlob
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
text = 'The senators supporting the leader failed to praise his hopeless HIV prevention program'
# Result of said parsing : Type (json)
output = stanford.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse', 'outputFormat': 'json'})

#This is the tree
s = output['sentences'][0]['parse']

# Reformatting as an NLTK obj same type as s
tree = Tree.fromstring(s)
#tree.pretty_print()

# Get the phrase from the tree
phrases = listify(tree)

# For each phrase in the parsed text
for phrase in phrases:
    print("---" + phrase[0] + "-----")
    # Iterate through the words in a phrase
    for i in range(1,len(phrase),2):

        # If odd amount of words in phrase the last word is on it's own
        if (i+1 == len(phrase)):
            # If our knowledge base has the word's sentiment
            if phrase[i] in basal_sentiment_dictionary:

                # Print the sentiment
                print(basal_sentiment_dictionary[phrase[i]])

            # If the the phrase is a known determiner
            elif phrase[i] in basal_determiner_bank:
                print('N')

            # If our knowledge base doesn't include this word then lookup the
            # the sentiment using textblob library
            else:
                # convert the word to a TextBlob friendly format
                word = TextBlob(phrase[i])

                # if the sentiment is 0 then print N
                if word.sentiment[0] == 0:
                    basal_sentiment_dictionary[phrase[i]] = 'N'
                    print('N')

                # If the sentiment is > 0 then print +
                elif word.sentiment[0] > 0:
                    basal_sentiment_dictionary[phrase[i]] = '+'
                    print('+')

                # If the sentiment is < 0 then print -
                elif word.sentiment[0] < 0:
                    basal_sentiment_dictionary[phrase[i]] = 'N'
                    print('-')

            print([phrase[i]])

        # If even then pair up words
        elif (len([phrase[i],phrase[i+1]]) == 2):

            # If our knowledge base has the word's sentiment
            if phrase[i] in basal_sentiment_dictionary:

                # Print the sentiment
                print(basal_sentiment_dictionary[phrase[i]])

            # If the the phrase is a known determiner
            elif phrase[i] in basal_determiner_bank:
                print('N')

            # If our knowledge base doesn't include this word then lookup the
            # the sentiment using textblob library
            else:
                # convert the word to a TextBlob friendly format
                word = TextBlob(phrase[i])

                # if the sentiment is 0 then print N
                if word.sentiment[0] == 0:
                    basal_sentiment_dictionary[phrase[i+1]] = 'N'
                    print('N')

                # If the sentiment is > 0 then print +
                elif word.sentiment[0] > 0:
                    basal_sentiment_dictionary[phrase[i+1]] = '+'
                    print('+')

                # If the sentiment is < 0 then print -
                elif word.sentiment[0] < 0:
                    basal_sentiment_dictionary[phrase[i+1]] = 'N'
                    print('-')

            # If our knowledge base has the word's sentiment
            if phrase[i+1] in basal_sentiment_dictionary:

                # Print the sentiment
                print(basal_sentiment_dictionary[phrase[i+1]])

            # If the word is a known determinmer
            elif phrase[i+1] in basal_determiner_bank:
                print('N')

            # If our knowledge base doesn't include this word then lookup the
            # the sentiment using textblob library
            else:
                # convert the word to a TextBlob friendly format
                word = TextBlob(phrase[i+1])

                # if the sentiment is 0 then print N
                if word.sentiment[0] == 0:
                    basal_sentiment_dictionary[phrase[i+1]] = 'N'
                    print('N')

                # If the sentiment is > 0 then print +
                elif word.sentiment[0] > 0:
                    basal_sentiment_dictionary[phrase[i+1]] = '+'
                    print('+')

                # If the sentiment is < 0 then print -
                elif word.sentiment[0] < 0:
                    basal_sentiment_dictionary[phrase[i+1]] = '-'
                    print('-')

            print([phrase[i],phrase[i+1]])
