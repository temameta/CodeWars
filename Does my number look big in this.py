def narcissistic( value ):
    is_narc = False
    new_val = 0
    length = len(str(value))
    for k in str(value):
        new_val+=int(k)**length
    if new_val==value:
        is_narc = True
    return is_narc
print(narcissistic(153))