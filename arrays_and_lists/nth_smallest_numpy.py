"""
Find nth smallest elements in an array and return them as a sorted array
desired_complexity: better than O(n log n)
difficulty: medium-easy
"""
import numpy as np

def find_nth_smallest(array, n):
	nth_smallest = np.full(n, float('inf'))
	for num in array:
		largest_i = np.argmax(nth_smallest)
		if num < nth_smallest[largest_i]:
			nth_smallest[largest_i] = num
	return sorted(nth_smallest)

large_list = np.random.randint(100000, size=10000)
print(find_nth_smallest(large_list, 10))

# PSEUDOCODE
# init array of smallest elements of n size
# for num in array
# get max of smallest elements
# if max is smaller then current num than swap them
# return smallest elements 