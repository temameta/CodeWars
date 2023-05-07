def head(a):
    return a[0]
def tail(a):
    b = [a[k] for k in range(1,len(a))]
    return b
def init(a):
    b = [a[k] for k in range(0, len(a)-1)]
    return b
def last(a):
    return a[-1]
