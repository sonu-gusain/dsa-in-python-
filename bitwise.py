#right sift operator 

def power_of_two(n):
    if n<=0:
        return 0
    else:
        while n > 1:
           if n%2!=0:
                return False
           n = n>>1
        return True
print(power_of_two(34))

#left sift operator

def power_of_two(num):
    if num<=0:
        return 0
    power = 1
    while power<num:
        power = power << 1
    return power == num
print(power_of_two(18))