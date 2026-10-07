"""Lesson 2 - strings, lists and dictionaries: the three data structures you use in every problem.

Run: python lessons/02_strings_lists_dicts.py
"""

# --- Strings -------------------------------------------------------------
s = "hacker rank"
print(len(s), s.upper(), s[0], s[-1])   # length, upper case, first and last char
print(s[0:6])                            # slicing: 'hacker'
print(s[::-1])                           # reversed string
print(s.split())                         # ['hacker', 'rank'] - used to parse input lines!
print("-".join(["a", "b", "c"]))         # 'a-b-c'

# --- Lists ---------------------------------------------------------------
nums = [5, 3, 8, 1]
nums.append(10)
print(nums, len(nums), nums[0], nums[-1])
print(sum(nums), min(nums), max(nums))
print(sorted(nums))                      # new sorted list, original unchanged
squares = [x * x for x in nums]          # list comprehension
print(squares)

# Parse a typical HackerRank line "1 2 3 4" into a list of ints:
line = "1 2 3 4"
values = list(map(int, line.split()))
print(values)

# --- Dictionaries (hash maps) -------------------------------------------
ages = {"ana": 25, "mihai": 30}
ages["ion"] = 22                          # add / update
print(ages["ana"], ages.get("nobody", 0))  # .get avoids KeyError
for key, value in ages.items():
    print(key, "->", value)
print("ana" in ages)                      # O(1) membership check

# --- Sets ----------------------------------------------------------------
seen = set([1, 2, 2, 3])
print(seen, 2 in seen)                    # duplicates removed, O(1) lookup
