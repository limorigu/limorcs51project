__author__ = 'Zac'

"""
This is the BK Tree implementation and the Levenshtein Distance calculator.
It supports adding words and txt files to the tree and querying the tree
for close matches of a string input. Each node will be a dictionary containing
a string, a frequency (number of appearances in passed-in texts), and another
dictionary containing the Node's children.
"""

class BKTree:

    global __MAX__
    __MAX__ = 1


    def __init__(self, distfn, words):
        """
        Creates a BK-tree from the given distance function and
        words list.
        distfn must take in two strings and return a non-negative
        integer value.
        words must be an iterable that can produce values to be passed to
        distfn
        """
        self.distfn = distfn

        it = iter(words)
        root = it.next()
        freq_init = 1
        self.tree = {'wd': root, 'fq': freq_init, 'cn': {}}

        # Add words to tree, getting rid of white space and punctuation
        for line in it:
            for wd in line.split():
                self._add_word(self.tree, wd.strip('.,;:!?"\'').lower())


    def _add_word(self, parent, word):
        """
        Recursively adds a word to the BK Tree. If the word is not already
        present, make a new node. If the word is present, update the
        frequency element of the node.
        """
        d = self.distfn(word, parent['wd'])
        global __MAX__

        # If word exists, update frequency
        if d == 0:
            parent['fq'] += 1
            if parent['fq'] > __MAX__ :
                __MAX__ = parent['fq']
        # If not, recurse down the tree and add a new node
        elif d in parent['cn']:
            self._add_word(parent['cn'][d], word)
        else:
            print("%s added!" % word)
            parent['cn'][d] = {'wd': word, 'fq': 1, 'cn': {}}


    def add_file(self, text):
        """
        Takes in a .txt file and adds every word (separated by white space)
        into the tree. Primarily used for updating word frequencies.
        """
        it = iter(text)
        for line in it:
            for wd in line.split():
                self._add_word(self.tree, wd.strip('.,;\":!?\'()').lower())


    def query(self, word, n):
        """
        Returns all nodes in the tree that are within edit distance `n'
        of `word`.
        Arguments:
         - word: a string to search the tree for
         - n: a non-negative integer. The maximum acceptable edit distance
              for returns.
        Return value: a list of tuples of the format
                      (Frequency proportion, Edit distance, word) in no
                      particular order.
        """
        # initialize the list to be returned in case of perfect match
        global match
        match = []
        # Helper function that recurses through the tree and adds acceptable
        # values to match
        def rec(parent):
            d = self.distfn(word.lower(), parent['wd'])
            results = []
            global __MAX__

            # If a perfect match is found, update frequency and global
            # match variable, then raise exception, stopping the recursion
            if d == 0:
                parent['fq'] += 1
                global match
                match = [(float(parent['fq']) / float(__MAX__), d, parent['wd'])]
                raise BaseException

            if d <= n:
                results.append((float(parent['fq']) / float(__MAX__), d, parent['wd'], ))

            for i in range(d-n, d+n+1):
                child = parent['cn'].get(i)
                if child is not None:
                    results.extend(rec(child))
            return results

        # If an exception was raised (perfect match found) return the match
        try:
            return rec(self.tree)
        except BaseException:
            return match

# Implementation from http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Levenshtein_distance#Python
def levenshtein(s, t):
    m, n = len(s), len(t)
    d = [range(n+1)]
    d += [[i] for i in range(1,m+1)]
    for i in range(0,m):
        for j in range(0,n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i+1].append( min(d[i][j+1]+1, # deletion
                               d[i+1][j]+1, #insertion
                               d[i][j]+cost) #substitution
                           )
    return d[m][n]

# Return an iterator that produces words in the given dictionary.
def dict_words(dictfile):
    return filter(len,
                   map(str.strip,
                        open(dictfile)))