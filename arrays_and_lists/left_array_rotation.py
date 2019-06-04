def array_left_rotation(a, k):
    return a[k:] + a[:k]
    
test1 = [44, 66, 35, 5879, 1]
answer = array_left_rotation(test1, 1)
assert answer == [66, 35, 5879, 1, 44]
