def listify(tree):
    # This contains the phrases from the tree type([[],[],..])
    phrases = []

    # For leaf in the subtrees in tree
    for leaf in tree.subtrees():
        # If the leaf is a noun phrase
        if leaf.label() == 'NP':

            #remove all child classifications
            leaf = leaf.flatten()
            phrase = []

            # For each word in the flattened leaf
            for word in leaf:
                ith_word = word
                # Appened each word in the leaf to the array phrase [" "," ",..]
                phrase.append(ith_word)
            if not phrases:
                # Add the annotation to the array at i[0]
                phrase.insert(0, 'NP')
                # Appened each word in the phrase to the array phrases " "," ",..]
                phrases.append(phrase)
                continue

            # For each array in phrases
            for listed_phrase in phrases:

                # If phrase is a subset of listed_phrase
                if set(phrase) < set(listed_phrase):
                    # Never append
                    ADD2LIST = False
                    break
                if not(set(phrase) < set(listed_phrase)):
                    # Speculate that we may append
                    ADD2LIST = True

            # If we left the loop and ADD2LIST is still True then its safe to
            # append
            if ADD2LIST == True:
                # Add the annotation to the array at i[0]
                phrase.insert(0, 'NP')
                phrases.append(phrase)

        # Works the same as the example above but with verb phrases
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
