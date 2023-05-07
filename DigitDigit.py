def digit(a):
    c = ""
    for k in range(len(str(a))):
        c+=str(int(str(a)[k])**2)
    return int(c)