def array_diff(a, b):
    return [k for k in a if k not in b]
print(array_diff([1,2],[1]))