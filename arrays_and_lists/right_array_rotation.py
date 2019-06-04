def right_rotation(array, n):
	return array[-n:] + array[:-n]

test1 = [44, 66, 35, 5879, 1]
answer = right_rotation(test1, 1)
print(answer)
assert answer == [1, 44, 66, 35, 5879]