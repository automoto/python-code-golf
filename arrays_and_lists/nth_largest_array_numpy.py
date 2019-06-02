"""
Find nth largest elements in an array and return them as a sorted array
desired_complexity: better than O(n log n)
difficulty: medium-easy

numpy solution is much faster when doing lookups for index of argmin/argmax versus (list.index(value))
ONLY against numpy arrays, this would be slower in a list
"""
import numpy as np

def find_nth_largest(array, n):
	nth_largest = np.full(n, float('-inf'))
	for num in array:
		min_i = np.argmin(nth_largest)
		if nth_largest[min_i] < num:
			nth_largest[min_i] = num
	return sorted(nth_largest)

large_list = np.random.randint(10000000, size=1000000)
print(find_nth_largest(large_list, 1000))