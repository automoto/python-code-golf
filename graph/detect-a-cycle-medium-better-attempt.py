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
	current_index = 0
	visited = 0
	
	while visited < len(array):
		if (visited > 0) and (current_index == 0):
			return False
		visited += 1
		current_index = nextIndex(current_index, array)
	return current_index == 0

# Note had to carefully handle edge cases of negative indexes on line 27 and 31
def nextIndex(current_index, array):
	jump = array[current_index]
	next = (current_index + jump) % len(array)
	if next >= 0:
		return next
	else:
		return next + len(array)
