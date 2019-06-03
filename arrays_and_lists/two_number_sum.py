"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. 
If no two numbers sum up to the target sum, the function should return an empty array. 
Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
"""

def twoNumberSum(array, targetSum):
	for index, current_num in enumerate(array):
		for index2, num_to_check in enumerate(array):
			if index == index2:
				continue
			if current_num + num_to_check == targetSum:
				return sorted([current_num, num_to_check])
	return []
test_array = [3, 5, -4, 8, 11, 1, -1, 6]
answer = twoNumberSum(test_array, 10)
assert answer == [-1, 11]