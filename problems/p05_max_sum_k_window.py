"""Problem 5 - Best K-Day Revenue (pattern: sliding window).

Given daily revenue for n days, find the maximum total over any k consecutive days.

Input:
    line 1: n and k separated by a space
    line 2: n space-separated integers (may be negative)
Output:
    the maximum sum of k consecutive values

Sample input:
6 3
2 1 5 1 3 2
Sample output:
9
"""


def max_window_sum(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))[:n]
    print(max_window_sum(arr, k))


if __name__ == "__main__":
    main()
