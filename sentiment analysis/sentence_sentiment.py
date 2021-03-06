from vote import vote
from group import group

def sentence_sentiment (words_as_polarity):

    print(words_as_polarity)

    while any(len(phrase) > 2 or type(phrase[1]) == tuple for phrase in words_as_polarity):

        words_as_polarity = group(words_as_polarity)

        words_as_polarity = vote(words_as_polarity)

        print (words_as_polarity)

    sentiments = []
    for i in range(0, len(words_as_polarity)):
        sentiments.append(words_as_polarity[i][1])
    sentence_sentiment = sum(sentiments)
    if sentence_sentiment == 0:
        print('sentence is neutral')
    elif sentence_sentiment > 0:
        print('sentence is positive')
    elif sentence_sentiment < 0:
        print('sentence is negative')

    return sentence_sentiment
