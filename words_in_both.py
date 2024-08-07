# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Pulls the words that are the same from two different strings of text.

def words_in_both(string1, string2)
    
    # Converts both strings of text into lowercase and splits them into sets of words
    set1 = set(string1.lower().split())
    set2 = set(string2.lower().split())
    
    # Finds the intersection of both sets ie. the dimilar words
    common_words = set1.intersection(set2)

    # Returns similar words
    return common_words
