from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past tense verbs both for single and plural.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    quantity = 1
    for _ in range(2):
        for _ in range(4):
            # Call the get_verb function which
            # should return a past verb, no matter the determiner.
            word = get_verb(quantity, "past")

            # Verify that the word returned from get_verb
            # is one of the words in the past_verbs list.
            assert word in past_verbs
        
        # Update the quantity for the second test
        quantity += 1

    # 2. Test the present tense verbs both for single and plural.

    present_single = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    present_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    quantity = 1
    for i in range(2):
        for _ in range(4):
            # Call the get_verb function which
            # should return a present verb.
            word = get_verb(quantity, "present")

            # Verify that the word returned from get_verb
            # is one of the words in the present_single list
            # if i == 0, meaning, the first iteration 
            # else check if the returned word is in the present_plural list.
            if i == 0:
                assert word in present_single
            else:
                assert word in present_plural
        
        # Update the quantity for the second test
        quantity += 1
    
    # 3. Test the future tense verbs both for single and plural.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    quantity = 1
    for _ in range(2):
        for _ in range(4):
            # Call the get_verb function which
            # should return a future verb, no matter the determiner.
            word = get_verb(quantity, "future")

            # Verify that the word returned from get_verb
            # is one of the words in the future_verbs list.
            assert word in future_verbs
        
        # Update the quantity for the second test
        quantity += 1


def test_get_preposition():
    # Test if the preposition returned is part of the list 
    # of prepositions specified in the get_preposition function

    prepositions = ["about", "above", "across", "after", "along",
       "around", "at", "before", "behind", "below",
       "beyond", "by", "despite", "except", "for",
       "from", "in", "into", "near", "of",
       "off", "on", "onto", "out", "over",
       "past", "to", "under", "with", "without"]
    
    # Get preposition and assert if it is in the list
    for _ in range(5):
        preposition = get_preposition()

        assert preposition in prepositions


def test_get_prepositional_phrase():
    # 1. Test if the prepositional phrase returned are four words
    # for both quantities 1 and 2

    phrase1 = get_prepositional_phrase(1)
    phrase2 = get_prepositional_phrase(2)

    phrase1 = phrase1.split()
    phrase2 = phrase2.split()

    assert len(phrase1) == 4
    assert len(phrase2) == 4

    # 2. Test if each of the words returned from the get_prepositional_phrase()
    # is the correct English part of the speech, "1" and "2" references the "quantity"

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    determiners1 = ["a", "one", "the"]
    determiners2 = ["some", "many", "the"]

    adjectives = ["happy", "sad", "brave", "clever", "thoughtful",
        "confident", "beautiful", "strong","joyful", "fearful", "calm", "mysterious",
        "generous", "curious", "fierce", "playful", "grateful", "sincere"]

    nouns1 = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    nouns2 = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(5):
        phrase1 = get_prepositional_phrase(1)
        phrase2 = get_prepositional_phrase(2)

        phrase1 = phrase1.split()
        phrase2 = phrase2.split()

        assert phrase1[0] in prepositions
        assert phrase1[1] in determiners1
        assert phrase1[2] in adjectives
        assert phrase1[3] in nouns1

        assert phrase2[0] in prepositions
        assert phrase2[1] in determiners2
        assert phrase2[2] in adjectives
        assert phrase2[3] in nouns2


def test_get_adjective():
    # Test if adjective returned is in
    # list of adjectives
    adjectives = ["happy", "sad", "brave", "clever", "thoughtful",
        "confident", "beautiful", "strong","joyful", "fearful", "calm", "mysterious",
        "generous", "curious", "fierce", "playful", "grateful", "sincere"]

    # Get adjective and assert if it is in the list
    for _ in range(5):
        adjective = get_adjective()

        assert adjective in adjectives 


def test_get_adverb():
    # Test if adverb returned is in
    # list of adverbs
    adverbs = ["quickly", "carefully", "happily", "sadly",
        "briskly", "loudly", "quietly", "suddenly", "gently", "swiftly",
        "cautiously", "proudly", "anxiously", "gracefully", "honestly",
        "silently", "joyfully", "patiently", "excitedly", "clearly"]

    # Get adverb and assert if it is in the list
    for _ in range(5):
        adverb = get_adverb()
    
        assert adverb in adverbs 


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
