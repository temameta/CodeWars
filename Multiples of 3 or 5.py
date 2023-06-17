def solution(number):
    sum = 0
    if number < 0: return 0
    if number >= 3:
        for k in range(3,number):
            if k%3==0 or k%5==0:
                sum+=k
    return sum