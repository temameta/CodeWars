def find_outlier(integers):
    parity = True
    if (integers[0]%2!=0 and integers[1]%2!=0) or (integers[1]%2!=0 and integers[2]%2!=0) or (integers[0]%2!=0 and integers[2]%2!=0):
        parity = False
    if parity:
        for k in integers:
            if k%2!=0:
                outlier = k
    else:
        for k in integers:
            if k%2==0:
                outlier = k
    return outlier