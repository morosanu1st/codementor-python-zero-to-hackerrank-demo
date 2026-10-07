"""Every lesson script must run cleanly, and the pattern helpers must be correct."""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

LESSONS = sorted((Path(__file__).resolve().parents[1] / "lessons").glob("*.py"))


def load(name):
    path = next(p for p in LESSONS if p.stem.endswith(name))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("path", LESSONS, ids=lambda p: p.name)
def test_lesson_runs(path):
    result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()


def test_fizzbuzz():
    m = load("loops_conditionals")
    assert m.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert m.fizzbuzz(15)[-1] == "FizzBuzz"


def test_frequency_helpers():
    m = load("frequency_counting")
    assert m.char_frequency("aab") == {"a": 2, "b": 1}
    assert m.first_unique_char("loveleetcode") == 2
    assert m.is_anagram("listen", "silent")


def test_two_pointer_helpers():
    m = load("two_pointers")
    assert m.is_palindrome("abba") and not m.is_palindrome("abc")
    assert m.pair_with_sum([1, 2, 4, 7, 11, 15], 15) == (4, 11)
    assert m.pair_with_sum([1, 2], 10) is None


def test_sliding_window_helpers():
    m = load("sliding_window")
    assert m.max_sum_window([2, 1, 5, 1, 3, 2], 3) == 9
    assert m.longest_unique_substring("pwwkew") == 3
    assert m.longest_unique_substring("") == 0


def test_sorting_helpers():
    m = load("sorting")
    assert m.min_abs_difference([3, -7, 0]) == 3
    assert m.merge_intervals([(1, 4), (4, 5)]) == [[1, 5]]
