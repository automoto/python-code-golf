"""
Find nth largest elements in an array and return them as a sorted array
desired_complexity: better than O(n log n)
difficulty: medium-easy

solution:
O(N * N * N + n log n) = O(N^3)
"""

def find_nth_largest(array, n):
	nth_largest = [float('-inf') for i in range(n)]
	for num in array:
		nth_largest_min = min(nth_largest)
		if nth_largest_min < num:
			i_min = nth_largest.index(nth_largest_min)
			nth_largest[i_min] = num
	return sorted(nth_largest)


import random
large_list = random.sample(range(1, 10000000), 1000000)
print(find_nth_largest(large_list, 1000))

# initiate a array of nth largest
# loop through each num in array
# get current min of largest
# if the min is less than the num
# swap the num into the nth largest
# return a sorted list of nth largest