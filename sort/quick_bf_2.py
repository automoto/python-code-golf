def quick_sort(arr):
	#base case
	if(len(arr) < 2):
		return arr
	pivot = arr[0]
	less = [i for i in arr[1:] if i < pivot]
	greater = [i for i in arr[1:] if i >= pivot]
	return quick_sort(less) + [pivot] + quick_sort(greater)

test_list = [44, 2056, 2, 2, 41, 109, 33, 32, 22, 67]
result = quick_sort(test_list)
print(result)