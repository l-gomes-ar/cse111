# Exceeding Requirements: To achieve this, I called the get_prepositional_phrase function
# twice in main, I defined and used both get_adjective and get_adverb functions
# (called get_adjective in the get_prepositional_phrase function as well) and created 
# the test functions for both of them as well as updating the test_get_prepositional_phrase.
import random


def main():
    # Generate and print six sentences with these characterstics: 
    # single - (past, present, and future)
    # plural - (past, present, and future)
    tenses = ["past", "present", "future"]

    # Loop and print the sentences, three at a time,
    # three being "single" (past, present, and future)
    # and the other three "plural" for the same tenses
    for i in range(1, 3):
        for j in range(3):
            # Get each tense in order
            # Get the words, the quantity being i (1 and 2)
            tense = tenses[j]
            determiner = get_determiner(i)
            adjective = get_adjective()
            noun = get_noun(i)
            adverb = get_adverb()
            verb = get_verb(i, tense)
            prepositional_phrase1 = get_prepositional_phrase(i)
            prepositional_phrase2 = get_prepositional_phrase(i)
            
            print(f"{determiner} {adjective} {noun} {prepositional_phrase1} {verb} {adverb} {prepositional_phrase2}.".capitalize())
        

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    # Randomly choose and return a word 
    word = random.choice(words)
    return word


def get_preposition():
    """Returns a randomly chosen preposition 
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(prepositions)

    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.

    Return: a prepositional phrase.
    """
    # Get preposition, determiner, and noun
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {adjective} {noun}"

    return prepositional_phrase


def get_adjective():
    """Returns one randomly chosen adjective
    from this list of adjectives:
        "happy", "sad", "brave", "clever", "thoughtful",
        "confident", "beautiful", "strong","joyful", "fearful", "calm", "mysterious",
        "generous", "curious", "fierce", "playful", "grateful", "sincere"

    Return: a randomly chosen adjective.
    """
    adjectives = ["happy", "sad", "brave", "clever", "thoughtful",
        "confident", "beautiful", "strong","joyful", "fearful", "calm", "mysterious",
        "generous", "curious", "fierce", "playful", "grateful", "sincere"]
    
    adjective = random.choice(adjectives)

    return adjective


def get_adverb():
    """Returns one randomly chosen adverb
    from this list of adverbs:
        "quickly", "carefully", "happily", "sadly",
        "briskly", "loudly", "quietly", "suddenly", "gently", "swiftly",
        "cautiously", "proudly", "anxiously", "gracefully", "honestly",
        "silently", "joyfully", "patiently", "excitedly", "clearly"

    Return: a randomly chosen adverb.
    """

    adverbs = ["quickly", "carefully", "happily", "sadly",
        "briskly", "loudly", "quietly", "suddenly", "gently", "swiftly",
        "cautiously", "proudly", "anxiously", "gracefully", "honestly",
        "silently", "joyfully", "patiently", "excitedly", "clearly"]
    
    adverb = random.choice(adverbs)
    
    return adverb


if __name__ == "__main__":
    main()
