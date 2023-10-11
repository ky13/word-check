#!/usr/bin/env python3

from sys import argv
import re

WORDS_PATH = "./words.txt"

class Words():
    def __init__(self, pattern, bad):
        self.size = len(pattern)
        self.good = '[^' + ''.join(set(pattern.replace('.', ''))) + ']'
        self.bad = '[' + bad + ']'
        self.pattern = ('^'+pattern+'$').replace('.', self.good)
        self.words = []
        self.load()

    def load(self, path=WORDS_PATH):
        with open(path, "r") as f:
            for w in f:
                w = w.strip()
                if self.check(w):
                    self.words.append(w)

    def check(self, w):
        return re.match(self.pattern, w) and not re.search(self.bad, w)

    def get_words_string(self, n):
        return " ".join(self.words[n])

    def print(self):
        for w in self.words:
            print(w)

if __name__ == '__main__':

    Words(argv[1], argv[2]).print()
