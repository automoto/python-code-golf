"""
https://www.algoexpert.io/questions/Nth%20Fibonacci
Write a function that takes in an integer n and returns the nth Fibonacci number.
Example Input: 6
Output: 5(0, 1, 1, 2, 3, 5)
"""

def getNthFib(n):
	fib_sequence = [0, 1]
	for num in range(n):
		if(num <= 1):
			continue
		current_length = len(fib_sequence)
		last_num = fib_sequence[current_length - 1]
		second_to_last_num = fib_sequence[current_length - 2]
		fib_sequence.append(last_num + second_to_last_num)
	return fib_sequence[n - 1]

"""
PSEUDO-CODE
store a list of every digit in the fib sequence until the input
generate an iterator for Nth number in sequence
loop until the iterator is higher then the input
generate each number in sequence by summing up the previous two numbers
return number in fib sequence for input
"""	
