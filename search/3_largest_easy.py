"""
Write a function that takes in an array of integers and returns a sorted array of the three largest integers
in the input array. Note that the function should return duplicate integers if necessary;
for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
"""

def findThreeLargestNumbers(array):
    # Write your code here.
	# put the highest three in a array
	highest_three = [float('-inf'), float('-inf'), float('-inf')]
	# loop through each num in array
	for i, num in enumerate(array):
	# if num is higher then any in highest three, swap it into highest three
		current_low = min(highest_three)
		if current_low < num:
			current_low_i = highest_three.index(current_low)
			highest_three[current_low_i] = num
	# return the highest three
	return sorted(highest_three)