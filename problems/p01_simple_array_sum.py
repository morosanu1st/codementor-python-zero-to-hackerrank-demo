"""Problem 1 - Simple Array Sum (warm-up: reading input correctly).

Input:
    line 1: n, the number of elements
    line 2: n space-separated integers
Output:
    the sum of the elements

Sample input:
6
1 2 3 4 10 11
Sample output:
31
"""


def simple_array_sum(ar):
    return sum(ar)


def main():
    n = int(input().strip())
    ar = list(map(int, input().split()))[:n]
    print(simple_array_sum(ar))


if __name__ == "__main__":
    main()
