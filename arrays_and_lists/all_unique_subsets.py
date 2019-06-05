"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

import itertools
def subsets(nums):
    subsets = []
    for i in range(len(nums)):
        combinations = [list(i) for i in itertools.combinations(nums, i)]
        subsets.extend(combinations)
    subsets.append(nums)
    return subsets

answer = subsets([1, 2, 3])
print(answer)
assert answer == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]