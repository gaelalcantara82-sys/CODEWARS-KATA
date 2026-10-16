def repeats(arr):
    from functools import reduce
    return reduce((lambda x, y: x + y), [item for item in arr if arr.count(item)==1])
