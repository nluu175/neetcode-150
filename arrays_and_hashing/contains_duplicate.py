# https://leetcode.com/problems/contains-duplicate/
# https://note.nkmk.me/en/python-in-basic/#:~:text=source%3A%20in_timeit.py-,Fast%20for%20sets%3A%20O(1),on%20the%20number%20of%20elements.&text=Execution%20time%20does%20not%20change%20depending%20on%20the%20value%20to%20look%20for.

from typing import List


def sol(nums: List[int]) -> bool:
    # Hash map
    # - Time O(n)
    # - Space O(n)
    numbers = {}

    for i in nums:
        if i in numbers:
            return True
        else:
            numbers[i] = 0

    return False


# Brute force: O(n^2) time and O(1) space

# Approach 1: Sort
# Only needs to iterate once
# Take O(nlogn) time and O(1) space


def nc_sol(nums: List[int]) -> bool:
    # set() in python is a hashmap
    # Each "in" check takes O(1) time
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False
