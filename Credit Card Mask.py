def maskify(a):
    if len(a) > 4:
        return "#"*(len(a)-4) + a[(len(a)-4):]
    return a