"""Lesson 8 - Pattern: sorting first.

Sorting costs O(n log n) but often makes the rest of the problem trivial.
Run: python lessons/08_sorting.py
"""


def min_abs_difference(nums):
    """After sorting, the closest pair is always adjacent."""
    nums = sorted(nums)
    return min(b - a for a, b in zip(nums, nums[1:]))


def sort_by_frequency_then_value(nums):
    from collections import Counter
    counts = Counter(nums)
    return sorted(nums, key=lambda x: (-counts[x], x))   # custom sort key


def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = [list(intervals[0])]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    print(min_abs_difference([3, -7, 0]))                         # 3
    print(sort_by_frequency_then_value([4, 6, 2, 6, 4, 4]))       # [4, 4, 4, 6, 6, 2]
    print(merge_intervals([(1, 3), (8, 10), (2, 6), (15, 18)]))   # [[1, 6], [8, 10], [15, 18]]
    words = ["banana", "kiwi", "apple"]
    print(sorted(words, key=len), sorted(words, reverse=True))
