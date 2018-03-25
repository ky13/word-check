#!/usr/bin/env python3

from sys import argv
from re import match

WORDS_PATH = "/usr/share/dict/words"

class Words():
    def __init__(self, letters):
        self.letters = letters
        self.counts = {a: letters.count(a) for a in letters}
        self.words = {n+1: [] for n in range(len(letters))}
        self.load()

    def load(self, path=WORDS_PATH):
        with open(path, "r") as f:
            for w in f:
                w = w.strip()
                pattern = '^'+"[{0}]".format(self.letters)*len(w)+'$'
                if match(pattern, w) and all([w.count(a) <= n for a,n, in self.counts.items()]):
                    self.words[len(w)].append(w)

    def get_words_string(self, n):
        return " ".join(self.words[n])

    def print_n(self,n):
        print("{0}\n{1}-letter words\n\n  {2}\n".format("="*40, n, self.get_words_string(n)))

    def print(self):
        for n in range(len(self.letters), 2, -1):
            self.print_n(n)

if __name__ == '__main__':

    Words(argv[1]).print()
