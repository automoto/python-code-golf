"""
You are given an array of integers. Each integer represents a jump of its value in the array. For instance, 
the integer 2 represents a jump of 2 indices forward in the array; the integer -3 represents a jump of 3 indices
backward in the array. If a jump spills past the array's bounds, it wraps over to the other side.
For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at
the last index in the array brings us to index 0. Write a function that returns a boolean representing whether
the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps,
every element is visited exactly once before landing back on the starting index.

input = [2, 3, 1, -4, -4, 2]
output = True
"""
def hasSingleCycle(array):
	search = True
	cycleFound = False
	count = 0
	jump = 0
	array_len = len(array)
	while search:
		if(count > array_len):
			cycleFound = array.index(next) == 0
			search = False
		next = array[jump]
		jump = next
		count += 1
	return cycleFound

