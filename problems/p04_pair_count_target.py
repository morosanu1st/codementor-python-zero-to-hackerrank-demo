"""Problem 4 - Count Pairs With Target Sum (pattern: sorting + two pointers).

Count the pairs of positions i < j with arr[i] + arr[j] == k.

Input:
    line 1: n and k separated by a space
    line 2: n space-separated integers
Output:
    the number of pairs

Sample input:
5 6
1 5 7 -1 5
Sample output:
3
"""


def count_pairs(arr, k):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    pairs = 0
    while left < right:
        total = arr[left] + arr[right]
        if total < k:
            left += 1
        elif total > k:
            right -= 1
        elif arr[left] == arr[right]:
            # every element between left and right is the same value
            m = right - left + 1
            pairs += m * (m - 1) // 2
            break
        else:
            lv, rv = arr[left], arr[right]
            lc = rc = 0
            while arr[left] == lv:
                lc += 1
                left += 1
            while arr[right] == rv:
                rc += 1
                right -= 1
            pairs += lc * rc
    return pairs


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))[:n]
    print(count_pairs(arr, k))


if __name__ == "__main__":
    main()
