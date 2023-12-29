# https://leetcode.com/problems/two-sum/description/


def sol(nums, target):
    # hash table
    # time: O(n)
    # space: O(n)
    nums_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [i, nums_dict[complement]]
        else:
            nums_dict[num] = i

        print(num)
        print(nums_dict)

# nc solution
# approach 1: iterate, for each value, check all 
# other to see if they sum up the target
# time O(n^2)

nums = [2, 7, 11, 15]
target = 9

sol(nums, target)
