"""Problem 6 - Minimum Absolute Difference in an Array (pattern: sorting).

Input:
    line 1: n
    line 2: n space-separated integers
Output:
    the minimum |arr[i] - arr[j]| over all pairs i != j

Sample input:
3
3 -7 0
Sample output:
3

Brute force is O(n^2) and times out for n = 10^5; sorting makes it O(n log n),
because the closest pair must be neighbours in sorted order.
"""


def minimum_absolute_difference(arr):
    arr = sorted(arr)
    return min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))


def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))[:n]
    print(minimum_absolute_difference(arr))


if __name__ == "__main__":
    main()
