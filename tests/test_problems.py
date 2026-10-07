"""Tests for the HackerRank-style solutions.

Two levels, like HackerRank itself:
  1. unit tests on the function you implement
  2. end-to-end tests that feed stdin and compare stdout exactly
"""
import random
import subprocess
import sys
from itertools import combinations
from pathlib import Path

import pytest

from problems.p01_simple_array_sum import simple_array_sum
from problems.p02_sales_by_match import sock_merchant
from problems.p03_making_anagrams import make_anagram
from problems.p04_pair_count_target import count_pairs
from problems.p05_max_sum_k_window import max_window_sum
from problems.p06_min_abs_difference import minimum_absolute_difference

ROOT = Path(__file__).resolve().parents[1]


def run(script, stdin):
    result = subprocess.run(
        [sys.executable, str(ROOT / "problems" / script)],
        input=stdin, capture_output=True, text=True, check=True,
    )
    return result.stdout


@pytest.mark.parametrize("script, stdin, expected", [
    ("p01_simple_array_sum.py", "6\n1 2 3 4 10 11\n", "31\n"),
    ("p02_sales_by_match.py", "9\n10 20 20 10 10 30 50 10 20\n", "3\n"),
    ("p03_making_anagrams.py", "cde\nabc\n", "4\n"),
    ("p04_pair_count_target.py", "5 6\n1 5 7 -1 5\n", "3\n"),
    ("p05_max_sum_k_window.py", "6 3\n2 1 5 1 3 2\n", "9\n"),
    ("p06_min_abs_difference.py", "3\n3 -7 0\n", "3\n"),
    # input without trailing newline / with extra spaces, as HackerRank sometimes sends
    ("p01_simple_array_sum.py", "3\n 1  2 3 ", "6\n"),
])
def test_sample_io(script, stdin, expected):
    assert run(script, stdin) == expected


def test_simple_array_sum_edge_cases():
    assert simple_array_sum([0]) == 0
    assert simple_array_sum([-5, 5]) == 0
    assert simple_array_sum([10**9] * 5) == 5 * 10**9   # Python ints never overflow


def test_sock_merchant():
    assert sock_merchant(1, [7]) == 0
    assert sock_merchant(4, [1, 1, 1, 1]) == 2
    assert sock_merchant(5, [1, 2, 1, 2, 1]) == 2


def test_make_anagram():
    assert make_anagram("abc", "cba") == 0
    assert make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") == 30
    assert make_anagram("a", "b") == 2


def brute_pairs(arr, k):
    return sum(1 for a, b in combinations(arr, 2) if a + b == k)


def test_count_pairs_examples():
    assert count_pairs([1, 1, 1, 1], 2) == 6
    assert count_pairs([1, 2, 3], 10) == 0
    assert count_pairs([3, 3, 3, 3, 3, 3], 6) == 15


def test_count_pairs_matches_brute_force():
    rng = random.Random(0)
    for _ in range(300):
        arr = [rng.randint(-5, 5) for _ in range(rng.randint(0, 12))]
        k = rng.randint(-6, 6)
        assert count_pairs(arr, k) == brute_pairs(arr, k), (arr, k)


def test_max_window_sum():
    assert max_window_sum([5], 1) == 5
    assert max_window_sum([-3, -1, -2], 2) == -3      # all negative
    assert max_window_sum([1, 2, 3, 4], 4) == 10      # window == whole array
    rng = random.Random(1)
    for _ in range(200):
        arr = [rng.randint(-20, 20) for _ in range(rng.randint(1, 15))]
        k = rng.randint(1, len(arr))
        expected = max(sum(arr[i:i + k]) for i in range(len(arr) - k + 1))
        assert max_window_sum(arr, k) == expected


def test_minimum_absolute_difference():
    assert minimum_absolute_difference([1, 1]) == 0
    assert minimum_absolute_difference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1
    assert minimum_absolute_difference([1, -3, 71, 68, 17]) == 3


def test_minimum_absolute_difference_is_fast_on_large_input():
    import time
    arr = list(range(0, 2 * 10**5, 2))
    start = time.perf_counter()
    assert minimum_absolute_difference(arr) == 2
    assert time.perf_counter() - start < 1.0
