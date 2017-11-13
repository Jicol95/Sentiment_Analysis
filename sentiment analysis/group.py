def group(post_vote_list):
    frazes = []
    # For each phrase in the parsed text
    for phrase in post_vote_list:
        words_to_symbols = []

        words_to_symbols.append(phrase[0])

        # Iterate through the words in a phrase
        for i in range(1,len(phrase),2):
            if (i+1 == len(phrase)):
                words_to_symbols.append(phrase[i])

            # If even then pair up words
            elif (len([phrase[i],phrase[i+1]]) == 2):
                words_to_symbols.append(tuple((phrase[i],phrase[i+1])))

        frazes.append(words_to_symbols)

    return frazes
