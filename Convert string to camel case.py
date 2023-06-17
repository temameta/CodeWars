import re
def to_camel_case(text):
    a = re.split("-|_", text)
    newText = a[0]
    for k in range(1,len(a)):
        newText+=a[k].capitalize()
    return newText
