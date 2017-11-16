#Sentiment dictionary
import re



def read_files(sentimentDictionary):

    posDictionary = open('../Corpora/positive-words.txt', 'r', encoding="ISO-8859-1")
    posWordList = re.findall(r"[a-z\-]+", posDictionary.read())

    negDictionary = open('../Corpora/negative-words.txt', 'r', encoding="ISO-8859-1")
    negWordList = re.findall(r"[a-z\-]+", negDictionary.read())

    for i in posWordList:
        sentimentDictionary[i] = "+"
    for i in negWordList:
        sentimentDictionary[i] = "-"

def read_det_file():

    determiners = open('../Corpora/det-words.txt', 'r', encoding="ISO-8859-1")
    determiner_bank = re.findall(r"[a-z\-]+", determiners.read())
    return determiner_bank

def read_negate_file():

    negators = open('../Corpora/NegationWords.txt', 'r', encoding="ISO-8859-1")
    negators_bank = re.findall(r"[a-z\-]+", negators.read())
    return negators_bank
