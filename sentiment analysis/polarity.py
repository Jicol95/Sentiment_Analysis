from textblob import TextBlob
def polarity(phrases, basal_sentiment_dictionary, basal_determiner_bank):
    frazes = []
    # For each phrase in the parsed text
    for phrase in phrases:

        words_to_symbols = []
        words_to_symbols.append(phrase[0])

        # Iterate through the words in a phrase
        for i in range(1,len(phrase),2):

            # If odd amount of words in phrase the last word is on it's own
            if (i+1 == len(phrase)):
                # If our knowledge base has the word's sentiment
                if phrase[i] in basal_sentiment_dictionary:

                    # Print the sentiment
                    if basal_sentiment_dictionary[phrase[i]] == 'N':
                        phrase[i] = 0
                    elif basal_sentiment_dictionary[phrase[i]] == '+':
                        phrase[i] = 1
                    elif basal_sentiment_dictionary[phrase[i]] == '-':
                        phrase[i] = -1

                # If the the phrase is a known determiner
                elif phrase[i] in basal_determiner_bank:
                    phrase[i] = 0
                    # print('N')

                # If our knowledge base doesn't include this word then lookup the
                # the sentiment using textblob library
                else:
                    # convert the word to a TextBlob friendly format
                    word = TextBlob(phrase[i])

                    # if the sentiment is 0 then print N
                    if word.sentiment[0] == 0:
                        basal_sentiment_dictionary[phrase[i]] = 'N'
                        phrase[i] = 0
                        # print('N')

                    # If the sentiment is > 0 then print +
                    elif word.sentiment[0] > 0:
                        basal_sentiment_dictionary[phrase[i]] = '+'
                        phrase[i] = 1
                        # print('+')

                    # If the sentiment is < 0 then print -
                    elif word.sentiment[0] < 0:
                        basal_sentiment_dictionary[phrase[i]] = '-'
                        phrase[i] = -1
                        # print('-')
                words_to_symbols.append(phrase[i])
                if i == len(phrases)-1:
                    frazes.append(words_to_symbols)
                # print([phrase[i]])

            # If even then pair up words
            elif (len([phrase[i],phrase[i+1]]) == 2):

                # If our knowledge base has the word's sentiment
                if phrase[i] in basal_sentiment_dictionary:

                    # Print the sentiment
                    if basal_sentiment_dictionary[phrase[i]] == 'N':
                        phrase[i] = 0
                    elif basal_sentiment_dictionary[phrase[i]] == '+':
                        phrase[i] = 1
                    elif basal_sentiment_dictionary[phrase[i]] == '-':
                        phrase[i] = -1

                # If the the phrase is a known determiner
                elif phrase[i] in basal_determiner_bank:
                    phrase[i] = 0
                    # print('N')

                # If our knowledge base doesn't include this word then lookup the
                # the sentiment using textblob library
                else:
                    # convert the word to a TextBlob friendly format
                    word = TextBlob(phrase[i])

                    # if the sentiment is 0 then print N
                    if word.sentiment[0] == 0:
                        basal_sentiment_dictionary[phrase[i+1]] = 'N'
                        phrase[i] = 0
                        # print('N')

                    # If the sentiment is > 0 then print +
                    elif word.sentiment[0] > 0:
                        basal_sentiment_dictionary[phrase[i+1]] = '+'
                        phrase[i] = 1
                        # print('+')

                    # If the sentiment is < 0 then print -
                    elif word.sentiment[0] < 0:
                        basal_sentiment_dictionary[phrase[i+1]] = 'N'
                        phrase[i] = -1
                        # print('-')

                # If our knowledge base has the word's sentiment
                if phrase[i+1] in basal_sentiment_dictionary:

                    # Print the sentiment
                    if basal_sentiment_dictionary[phrase[i+1]] == 'N':
                        phrase[i+1] = 0
                    elif basal_sentiment_dictionary[phrase[i+1]] == '+':
                        phrase[i+1] = 1
                    elif basal_sentiment_dictionary[phrase[i+1]] == '-':
                        phrase[i+1] = -1

                # If the word is a known determinmer
                elif phrase[i+1] in basal_determiner_bank:
                    phrase[i+1] = 0
                    # print('N')

                # If our knowledge base doesn't include this word then lookup the
                # the sentiment using textblob library
                else:
                    # convert the word to a TextBlob friendly format
                    word = TextBlob(phrase[i+1])

                    # if the sentiment is 0 then print N
                    if word.sentiment[0] == 0:
                        basal_sentiment_dictionary[phrase[i+1]] = 'N'
                        phrase[i+1] = 0
                        # print('N')

                    # If the sentiment is > 0 then print +
                    elif word.sentiment[0] > 0:
                        basal_sentiment_dictionary[phrase[i+1]] = '+'
                        phrase[i+1] = 1
                        # print('+')

                    # If the sentiment is < 0 then print -
                    elif word.sentiment[0] < 0:
                        basal_sentiment_dictionary[phrase[i+1]] = '-'
                        phrase[i+1] = -1
                        # print('-')
                words_to_symbols.append(tuple((phrase[i],phrase[i+1])))
                if i == len(phrases)-1:
                    frazes.append(words_to_symbols)
            # print(phrase)
            # print(words_to_symbols)

    return frazes
