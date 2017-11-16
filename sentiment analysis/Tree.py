def listify(tree, basal_sentiment_dictionary, negators_bank):
    # This contains the phrases from the tree type([[],[],..])
    phrases = []
    INs = []
    VBDs = []
    VBs = []
    ADVPs = []
    ADJPs = []
    RBs = []
    CCs = []
    JJs = []

    # For leaf in the subtrees in tree
    for leaf in tree.subtrees():

        if leaf.label() == 'CC':
            CCs.append(str(leaf[:2][0]))

        if leaf.label() == 'IN':
            INs.append(str(leaf[:2][0]))

        if leaf.label() == 'JJ':
            leaf = leaf.flatten()
            JJs.append(str(leaf[:2][0]))

        if leaf.label() == 'ADVP':
            leaf = leaf.flatten()
            ADVPs.append(str(leaf[:4][0]))

        if leaf.label() == 'VBD':
            VBDs.append(str(leaf[:3][0]))

        if leaf.label() == 'VB':
            VBs.append(str(leaf[:2][0]))

        if leaf.label() == 'RB':
            RBs.append(str(leaf[:2][0]))

        if leaf.label() == 'ADJP':
            leaf = leaf.flatten()
            ADJPs.append(str(leaf[:4][0]))


    for leaf in tree.subtrees():

        ALLOW_INVERSION = False
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
        if leaf.label() == 'CC':
            leaf = leaf.flatten()
            phrase = []
            ALLOW_INVERSION = False
            for word in leaf:

                if (word in CCs) and (word in negators_bank):
                    ith_word = word + '¬'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = True

                else:
                    ith_word = word
                    phrase.append(ith_word)

            if not phrases:
                phrase.insert(0, 'CC')
                phrases.append(phrase)
                continue
            for listed_phrase in phrases:
                if set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) - set(CCs) < set(listed_phrase):
                    ADD2LIST = False
                    break
                if not(set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) - set(CCs) < set(listed_phrase)):
                    ADD2LIST = True
            if ADD2LIST == True:
                phrase.insert(0, 'CC')
                phrases.append(phrase)

        # Works the same as the example above but with verb phrases
        if leaf.label() == 'ADVP':
            leaf = leaf.flatten()
            phrase = []
            ALLOW_INVERSION = False
            for word in leaf:

                if (word in CCs) and (word in negators_bank):
                    ith_word = word + '¬'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = True

                else:
                    ith_word = word
                    phrase.append(ith_word)

            if not phrases:
                phrase.insert(0, 'ADVP')
                phrases.append(phrase)
                continue
            for listed_phrase in phrases:
                if set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) - set(CCs) < set(listed_phrase):
                    ADD2LIST = False
                    break
                if not(set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) - set(CCs) < set(listed_phrase)):
                    ADD2LIST = True
            if ADD2LIST == True:
                phrase.insert(0, 'ADVP')
                phrases.append(phrase)


        # Works the same as the example above but with verb phrases
        if leaf.label() == 'VP':
            leaf = leaf.flatten()
            phrase = []
            ALLOW_INVERSION = False
            for word in leaf:

                if word in negators_bank:
                    ith_word = word + '¬'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = True
                    continue

                if (word in JJs) and (ALLOW_INVERSION == True) and (word in basal_sentiment_dictionary):
                    ith_word = word + ' <¬>'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = False

                elif (word in RBs) and (ALLOW_INVERSION == True) and (word in basal_sentiment_dictionary):
                    ith_word = word + ' <¬>'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = False

                elif (word in VBs) and (ALLOW_INVERSION == True) and (word in basal_sentiment_dictionary):
                    ith_word = word + ' <¬>'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = False

                elif (word in ADJPs) and (ALLOW_INVERSION == True and word in basal_sentiment_dictionary):
                    ith_word = word + ' <¬>'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = False

                elif (word in VBDs) and (ALLOW_INVERSION == True and word in basal_sentiment_dictionary):
                    ith_word = word + ' <¬>'
                    phrase.append(ith_word)
                    ALLOW_INVERSION = False

                else:
                    ith_word = word
                    phrase.append(ith_word)

            if not phrases:
                phrase.insert(0, 'VP')
                phrases.append(phrase)
                continue
            for listed_phrase in phrases:
                if set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) < set(listed_phrase):
                    ADD2LIST = False
                    break
                if not(set(phrase) - set(VBDs) - set(VBs) - set(ADJPs) < set(listed_phrase)):
                    ADD2LIST = True
            if ADD2LIST == True:
                phrase.insert(0, 'VP')
                phrases.append(phrase)


    print (phrases)
    return phrases
