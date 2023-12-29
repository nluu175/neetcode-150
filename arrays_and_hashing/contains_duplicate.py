# https://leetcode.com/problems/contains-duplicate/


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
    pass
