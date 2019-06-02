def binary_search(array, target):
	# return a search with the array, target, starting and ending pointers
	return search(array, target, 0, len(array) - 1)

def search(array, target, start, end):
	# handle base case
	if(start > end):
		return - 1
	# get mid point
	mid = (start + end)//2
	# get guess and return target position if it matches
	guess = array[mid]
	if target == guess:
		return mid
	# if target is less than guess, search again with the start and the end thats less than the mid
	if target < guess:
		return search(array, target, start, mid - 1)
	 # if target is higher than guess, search again with the start above the mid and the end
	else:
		return search(array, target, mid + 1, end)



my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, 100))
