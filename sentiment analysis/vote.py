def vote(words_as_polarity):
    post_vote_list = []
    for phrase in words_as_polarity:
        votes_of_a_phrase = []
        for word_group in phrase:
            if type(word_group) == tuple:
                value = int(word_group[0]) + int(word_group[1])
                votes_of_a_phrase.append(value)

            else:
                votes_of_a_phrase.append(word_group)

        post_vote_list.append(votes_of_a_phrase)

    return post_vote_list
