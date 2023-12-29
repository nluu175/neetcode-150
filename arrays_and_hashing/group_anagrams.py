# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
from typing import List


def sol(strs: List[str]):
    # one pass
    # sort each, add to a dict
    # time O(n*nlogn)
    # space O(n)

    string_dict = {}
    for i, string in enumerate(strs):
        sorted_string = "".join(sorted(string))
        # print(sorted_string)
        if sorted_string in string_dict:
            string_dict[sorted_string].append(string)
        else:
            string_dict[sorted_string] = [string]

    return [string_dict[anagrams_list] for anagrams_list in string_dict]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = sol(strs=strs)
print(res)


def nc_sol(strs):
    # O(m * n) where m is the length of the given string
    # and n is the average length of each string

    # defaultdict(list) means "Defining a dictionary
    # with values as a list
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        print(count, s)

        res[tuple(count)].append(s)

    return res.values()


print(nc_sol(strs))
