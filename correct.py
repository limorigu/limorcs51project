__author__ = 'galkop'

"""
This is the main file, containing the code both for the correct function,
and for the various helper functions it uses
"""
# Import code from BK-tree library
import BK_TREE
import time
import math


"""
HELPER FUNCTION #1 -- takes in output of query, and returns the 7 highest
values from edit distance 1, as well as the 3 highest frequency values
from edit distance 2
"""
def subset_for_analysis(word,words):
    subset = []
    # define arrays for diff edit distances
    ones = [(f,e,w) for (f,e,w) in words if (e == 1)]
    twos = [(f,e,w) for (f,e,w) in words if (e == 2)]
    limit = min(7,len(ones))
    for i in range(limit):
        (bigf,bige,bigw) = max(ones)
        subset.append((bigf,bige,bigw))
        ones.remove((bigf,bige,bigw))
    limit2 = min(3,len(twos))
    for i in range(limit2):
        (bigf,bige,bigw) = max(twos)
        subset.append((bigf,bige,bigw))
        twos.remove((bigf,bige,bigw))
    return subset

"""
Correct Function -- takes in a list/dictionary of words, and returns most likely replacement.
Input is of the form [(edit#,freq1,word1),(edit#,freq2,word2),(edit#,freq3,word3),(edit#,freq4,word4),...]
"""
def correct(word,words):
    # First, narrow down possible words, and initialize the final list that will be analyzed.
    words_with_weights = subset_for_analysis(word,words)
    print(words_with_weights)
    # iterates through weighted words, and return most likely alternative
    final_weights = []
    for tup in words_with_weights:
        freq, ed, word = tup
        final_weights.append(((math.sqrt(freq)/(ed ** 4)), word))
    # store word with highest weight in word1, and return it
    _, word1 = max(final_weights)
    return word1