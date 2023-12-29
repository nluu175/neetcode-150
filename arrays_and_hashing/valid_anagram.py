# https://leetcode.com/problems/valid-anagram/


def solution(s: str, t: str) -> bool:
    # sort? then check if string is the same?
    # time O(nlogn) ?
    # space O(1)
    pass


def nc_sol_1(s, t):
    # approach 1: hashmap and count
    # time O(s+t)
    # space O(s+t) (worst case)
    # -> memory problem

    # approach 2:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(
            s[i], 0
        )  # 0 is default value if nothign is returned
        countS[t[i]] = 1 + countS.get(
            t[i], 0
        )  # 0 is default value if nothign is returned

    for c in countS:
        # check if the entries are similar
        if countS[c] != countT.get(c, 0):
            return False

    return True


def nc_sol_2(s, t):
    # approach 2: sort it
    # time O(nlogn)
    # space O(1)
    return sorted(s) == sorted(t)
