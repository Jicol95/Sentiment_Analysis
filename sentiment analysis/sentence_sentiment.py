from vote import vote
from group import group

def sentence_sentiment (words_as_polarity):

    print(words_as_polarity)

    while all(len(phrase) != 2 for phrase in words_as_polarity):


        words_as_polarity = vote(words_as_polarity)

        print(words_as_polarity)

        grouped_symbols = group(words_as_polarity)

        print(grouped_symbols)

        words_as_polarity = vote(grouped_symbols)

        print(words_as_polarity)

    if all(len(phrase) == 2 for phrase in words_as_polarity):
        sentence_sentiment = words_as_polarity[0][1] + words_as_polarity[1][1]
        if sentence_sentiment == 0:
            print('sentence is neutral')
        elif sentence_sentiment > 0:
            print('sentence is positive')
        elif sentence_sentiment < 0:
            print('sentence is negative')

    return sentence_sentiment
