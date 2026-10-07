# Python from Zero to HackerRank – tutoring demo

A small, runnable demo from **Mihai Chindriș** (Codementor mentor) for a complete Python beginner
who wants to pass a **HackerRank-style coding interview**.

It has two parts:
1. **Lessons**: short scripts that build up from `print()` to the four patterns behind most
   interview questions.
2. **Problems**: six HackerRank-style problems that read **stdin** and write **stdout** exactly
   the way HackerRank checks them, each with pytest tests.

## Contents

```
lessons/
  01_basics.py                 print, variables, types, arithmetic, f-strings, int(input())
  02_strings_lists_dicts.py    slicing, split/join, lists, comprehensions, dicts, sets
  03_functions.py              defining functions, defaults, returning several values
  04_loops_conditionals.py     for / while / if-elif-else, FizzBuzz
  05_frequency_counting.py     pattern: dict / Counter
  06_two_pointers.py           pattern: two pointers on sorted data
  07_sliding_window.py         pattern: fixed and variable sliding windows
  08_sorting.py                pattern: sort first, custom keys, merge intervals
problems/
  p01_simple_array_sum.py      warm-up: parse "n" and a line of ints
  p02_sales_by_match.py        frequency counting
  p03_making_anagrams.py       frequency counting on strings
  p04_pair_count_target.py     sorting + two pointers
  p05_max_sum_k_window.py      sliding window
  p06_min_abs_difference.py    sorting (O(n log n) instead of O(n^2))
tests/                         pytest: sample I/O end-to-end + edge cases + brute-force checks
```

## How to run

```bash
pip install pytest

# run a lesson
python lessons/01_basics.py

# run a problem the HackerRank way: input on stdin
echo -e "9\n10 20 20 10 10 30 50 10 20" | python problems/p02_sales_by_match.py   # -> 3
python problems/p06_min_abs_difference.py      # then type the input and press Ctrl+D

# run every test
pytest
```

Python 3.8+. The solutions use only the standard library.

## Week-by-week plan (about 8 weeks, 2 sessions a week)

| Week | Focus | You can do this by the end of the week |
|------|-------|-----------------------------------------|
| 1 | Setup, `print`, variables, types, arithmetic, `input()` | Read numbers from input and print a formatted result |
| 2 | Strings, lists, dicts, sets | Parse any HackerRank input line into the right structure |
| 3 | Conditionals, loops, functions | Solve "Easy" warm-ups (FizzBuzz, Simple Array Sum, Plus Minus) on your own |
| 4 | Frequency counting, Big-O basics | Sales by Match, Making Anagrams, Ransom Note |
| 5 | Sorting and two pointers | Pairs / two-sum variants, Minimum Absolute Difference |
| 6 | Sliding window, prefix sums, stacks and queues | Max-sum window, Balanced Brackets |
| 7 | Recursion, basic search (binary search, BFS/DFS intro), Medium problems | Two timed Medium problems in 45 min |
| 8 | Mock interviews under HackerRank conditions | Full timed mock test plus review of every mistake |

Between sessions: 3–5 problems a week on HackerRank (Interview Preparation Kit), which we review together.

## HackerRank tips

**Reading input**
- `input()` always returns a **string**, so convert it: `n = int(input())`.
- A line of numbers: `arr = list(map(int, input().split()))`. `split()` with no argument also
  handles extra spaces.
- Two values on one line: `n, k = map(int, input().split())`.
- Large input: `import sys; data = sys.stdin.read().split()` is faster than many `input()` calls.
- Print **exactly** what is asked: no extra text like `"Answer:"`, and watch the decimals
  (`f"{x:.6f}"`).

**Edge cases to always check**
- Smallest input (n = 1, an empty string), all-equal values, negative numbers and zero.
- Duplicates (see `p04`, where equal values form many pairs).
- The largest constraints: Python ints don't overflow, but slow loops time out.

**Time complexity**
- Read the constraints first. For n ≤ 10^5, you need roughly O(n) or O(n log n); a nested O(n²) loop will time out.
- `x in list` is O(n) and `x in set` / `x in dict` is O(1), so swap a list for a set in lookups.
- Sorting is O(n log n) and often turns the rest of the problem into a single pass.

**Process**
1. Restate the problem and work through the sample by hand.
2. Write the brute force first, then optimise using one of the four patterns.
3. Test the samples and your own edge cases before you submit.

## How sessions work

- **Length and cadence:** 60-minute live sessions, 2 a week, on screen share in your own editor.
- **Structure:** 10 min reviewing homework, 20 min on a new concept, 25 min solving a problem
  together (you type, I guide), 5 min agreeing on homework.
- **Homework:** 3–5 problems a week. Push them to GitHub or paste them in chat, and I'll review them with comments.
- **From week 6 on:** timed mock problems, where you explain your approach out loud the way you
  would in the real interview.
- **Async help:** quick questions in Codementor chat between sessions.

---
*Codementor demo by Mihai Chindriș*
