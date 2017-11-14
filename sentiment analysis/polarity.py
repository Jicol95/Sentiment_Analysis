from textblob import TextBlob
def polarity(phrases, basal_sentiment_dictionary, basal_determiner_bank):
    frazes = []
    # For each phrase in the parsed text
    for phrase in phrases:

        words_to_symbols = []
        words_to_symbols.append(phrase[0])

        # Iterate through the words in a phrase
        for i in range(1,len(phrase),2):
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
                phrase[i] = 0

            words_to_symbols.append(phrase[i])
            if i == len(phrases)-1:
                frazes.append(words_to_symbols)
            # print([phrase[i]])



    return frazes
