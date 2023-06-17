def move_zeros(lst):
    for k in lst:
        if k == 0:
            lst.append(0)
            lst.remove(0)
    return lst