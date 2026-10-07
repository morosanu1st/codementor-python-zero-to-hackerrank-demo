"""Lesson 3 - functions: name a piece of logic, give it inputs, return an output.

HackerRank gives you a function signature to complete, so this is the core skill.
Run: python lessons/03_functions.py
"""


def add(a, b):
    return a + b


def greet(name, greeting="Hello"):   # default argument
    return f"{greeting}, {name}!"


def min_and_max(numbers):
    """Functions can return several values (as a tuple)."""
    return min(numbers), max(numbers)


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print(add(2, 3))
    print(greet("Ana"))
    print(greet("Ana", greeting="Hi"))
    lo, hi = min_and_max([4, 9, 1, 7])
    print(lo, hi)
    print([n for n in range(10) if is_even(n)])
