from textblob import TextBlob
def polarity(phrases, basal_sentiment_dictionary, basal_determiner_bank):
    frazes = []
    # For each phrase in the parsed text
    phrase_counter = 0

    for j in range(0,len(phrases)):
        phrase = phrases[j]
        phrase_counter +=1
        words_to_symbols = []
        words_to_symbols.append(phrase[0])
        Effect = False

        # Iterate through the words in a phrase
        for i in range(1,len(phrase)):
            # If our knowledge base has the word's sentiment
            word = phrase[i]
            if word in basal_sentiment_dictionary and len(word) > 1:

                # Print the sentiment
                if basal_sentiment_dictionary[word] == 'N':
                    word = 0
                elif basal_sentiment_dictionary[word] == '+':
                    word = 1
                elif basal_sentiment_dictionary[word] == '-':
                    word = -1

            # If the the phrase is a known determiner
            elif word in basal_determiner_bank:
                word = 0
                # print('N')

            # Neutralize everything before but
            elif word == 'but¬':
                word = 0
                for k in range(0, j):
                    for l in range(1, len(frazes[k])):
                        frazes[k][l] = 0

            elif '¬' == word[-1] and word[:-1] in basal_sentiment_dictionary and len(word) > 1:
                if basal_sentiment_dictionary[word[:-1]] == 'N':
                    word = 0
                elif basal_sentiment_dictionary[word[:-1]] == '+':
                    word = 1
                elif basal_sentiment_dictionary[word[:-1]] == '-':
                    word = -1

            elif '<¬>' in word and word[:-4] in basal_sentiment_dictionary:
                if basal_sentiment_dictionary[word.replace(' <¬>', '').strip()] == 'N':
                    word = 0
                elif basal_sentiment_dictionary[word.replace(' <¬>', '').strip()]  == '+':
                    word = -1
                elif basal_sentiment_dictionary[word.replace(' <¬>', '').strip()] == '-':
                    word = 1

            else:
                word = 0
            words_to_symbols.append(word)

        frazes.append(words_to_symbols)
            # print([word])

        phrase_counter += 1
    return frazes
