"""Problem 2 - Sales by Match (pattern: frequency counting).

A pile of socks, each with a colour id. How many matching pairs are there?

Input:
    line 1: n, the number of socks
    line 2: n space-separated colour ids
Output:
    the number of pairs

Sample input:
9
10 20 20 10 10 30 50 10 20
Sample output:
3
"""
from collections import Counter


def sock_merchant(n, ar):
    return sum(count // 2 for count in Counter(ar).values())


def main():
    n = int(input().strip())
    ar = list(map(int, input().split()))
    print(sock_merchant(n, ar))


if __name__ == "__main__":
    main()
