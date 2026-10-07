"""Lesson 4 - loops and conditionals.

Run: python lessons/04_loops_conditionals.py
"""


def fizzbuzz(n):
    """Classic warm-up: returns the list of FizzBuzz strings from 1 to n."""
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def count_positive_negative_zero(nums):
    pos = neg = zero = 0
    for x in nums:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero


if __name__ == "__main__":
    print("\n".join(fizzbuzz(15)))

    # for with index and value
    for i, letter in enumerate("abc"):
        print(i, letter)

    # while loop: digits of a number
    n = 2026
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    print(digits[::-1])

    print(count_positive_negative_zero([-4, 3, -9, 0, 4, 1]))
