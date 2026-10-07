"""Lesson 7 - Pattern: sliding window.

For "best contiguous subarray / substring" questions: move a window along the
data and update the answer incrementally instead of recomputing from scratch.
Run: python lessons/07_sliding_window.py
"""


def max_sum_window(nums, k):
    """Largest sum of k consecutive elements (fixed-size window), O(n)."""
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]   # add the new element, drop the old one
        best = max(best, window)
    return best


def longest_unique_substring(s):
    """Length of the longest substring without repeating characters (variable window)."""
    last_seen = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1     # shrink the window past the repeat
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best


if __name__ == "__main__":
    print(max_sum_window([2, 1, 5, 1, 3, 2], 3))   # 9
    print(longest_unique_substring("abcabcbb"))    # 3
