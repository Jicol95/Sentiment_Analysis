def listify(tree):

    phrases = []

    for leaf in tree.subtrees():

        if leaf.label() == 'NP':
            leaf = leaf.flatten()
            phrase = []
            for word in leaf:
                ith_word = word
                phrase.append(ith_word)
            if not phrases:
                phrase.insert(0, 'NP')
                phrases.append(phrase)
                continue
            for listed_phrase in phrases:
                if set(phrase) < set(listed_phrase):
                    ADD2LIST = False
                    break
                if not(set(phrase) < set(listed_phrase)):
                    ADD2LIST = True
            if ADD2LIST == True:
                phrase.insert(0, 'NP')
                phrases.append(phrase)


        if leaf.label() == 'VP':
            leaf = leaf.flatten()
            phrase = []
            for word in leaf:
                ith_word = word
                phrase.append(ith_word)
            if not phrases:
                phrase.insert(0, 'VP')
                phrases.append(phrase)
                continue
            for listed_phrase in phrases:
                if set(phrase) < set(listed_phrase):
                    ADD2LIST = False
                    break
                if not(set(phrase) < set(listed_phrase)):
                    ADD2LIST = True
            if ADD2LIST == True:
                phrase.insert(0, 'VP')
                phrases.append(phrase)

    return phrases

def is_even(phrase):
    length = len(phrase)-1
    if length % 2 == 0:
        return True
    elif length % 2 == 1:
        return False
    elif length == 0:
        return False
