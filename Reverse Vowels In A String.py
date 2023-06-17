def reverse_vowels(s):
    vowels = "eyuioa"
    s_list = [k for k in s]
    vowels_in_string = [k for k in s if k in vowels]
    new_vowels_in_string = [vowels_in_string[k] for k in range(len(vowels_in_string)-1, -1, -1)]
    for k in range(len(s_list)):
        if s_list[k] in vowels:
            s_list[k] = new_vowels_in_string[0]
            new_vowels_in_string.pop(0)
    s = ""
    for k in s_list:
        s+=k
    return s