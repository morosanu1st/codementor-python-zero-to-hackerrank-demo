"""Lesson 6 - Pattern: two pointers.

Two indexes walking through the data (usually from both ends of a SORTED list)
replace a nested loop: O(n) instead of O(n^2).
Run: python lessons/06_two_pointers.py
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def pair_with_sum(sorted_nums, target):
    """Return a pair (a, b) from a sorted list with a + b == target, or None."""
    left, right = 0, len(sorted_nums) - 1
    while left < right:
        total = sorted_nums[left] + sorted_nums[right]
        if total == target:
            return sorted_nums[left], sorted_nums[right]
        if total < target:
            left += 1     # need a bigger sum
        else:
            right -= 1    # need a smaller sum
    return None


def remove_duplicates_sorted(nums):
    """Slow/fast pointers: unique values of a sorted list, keeping order."""
    if not nums:
        return []
    out = [nums[0]]
    for x in nums[1:]:
        if x != out[-1]:
            out.append(x)
    return out


if __name__ == "__main__":
    print(is_palindrome("racecar"), is_palindrome("hacker"))
    print(pair_with_sum([1, 2, 4, 7, 11, 15], 15))
    print(remove_duplicates_sorted([1, 1, 2, 3, 3, 3, 4]))
