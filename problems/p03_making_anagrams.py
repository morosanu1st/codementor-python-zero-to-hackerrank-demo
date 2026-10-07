"""Problem 3 - Making Anagrams (pattern: frequency counting).

Minimum number of character deletions so that two strings become anagrams.

Input:
    line 1: string a
    line 2: string b
Output:
    the minimum number of deletions

Sample input:
cde
abc
Sample output:
4
"""
from collections import Counter


def make_anagram(a, b):
    ca, cb = Counter(a), Counter(b)
    letters = set(ca) | set(cb)
    return sum(abs(ca[ch] - cb[ch]) for ch in letters)


def main():
    a = input().strip()
    b = input().strip()
    print(make_anagram(a, b))


if __name__ == "__main__":
    main()
