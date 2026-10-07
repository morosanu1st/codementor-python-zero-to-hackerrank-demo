"""Lesson 1 - Python basics: printing, variables, types, arithmetic, input.

Run: python lessons/01_basics.py
"""

# print() writes to the screen (stdout) - HackerRank checks exactly this output
print("Hello, HackerRank!")

# Variables just need a name and a value - no type declarations
age = 25            # int
price = 9.99        # float
name = "Ana"        # str
is_ready = True     # bool
print(type(age), type(price), type(name), type(is_ready))

# Arithmetic
print(7 + 2, 7 - 2, 7 * 2)
print(7 / 2)    # 3.5  -> true division always gives a float
print(7 // 2)   # 3    -> integer (floor) division
print(7 % 2)    # 1    -> remainder, great for "is it even?"
print(2 ** 10)  # 1024 -> power

# f-strings: the easiest way to format output
print(f"{name} is {age} years old")
print(f"Price with 2 decimals: {price:.2f}")

# Converting between types - input() ALWAYS gives you a string
text = "42"
number = int(text)
print(number + 1)       # 43
print(text + "1")       # "421" - string concatenation, a classic beginner bug

# On HackerRank you would read a value like this:
#   n = int(input())
