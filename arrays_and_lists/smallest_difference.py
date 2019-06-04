"""
Write a function that takes in two non-empty arrays of integers. The function should find the pair of
numbers (one from the first array, one from the second array) whose absolute difference is closest to zero.
The function should return an array containing these two numbers, with the number from the first array in the
first position. Assume that there will only be one pair of numbers with the smallest difference.
"""

def smallestDifference(arrayOne, arrayTwo):
	lowest_diff = float('inf')
	lowest_diff_pair = []
	for num1 in arrayOne:
		for num2 in arrayTwo:
			if num1 == num2:
				return [num1, num2]
			current_lowest = abs(num1 - num2)
			if current_lowest < lowest_diff:
				lowest_diff = current_lowest
				lowest_diff_pair = [num1, num2]
	return lowest_diff_pair

test1 = [-1, 5, 10, 20, 28, 3]
test2 = [26, 134, 135, 15, 17]
answer = smallestDifference(test1, test2)
assert answer == [28, 26]