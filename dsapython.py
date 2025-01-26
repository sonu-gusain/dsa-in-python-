def prime(n):
    if n == 1:
        return False
    if n==2:
        return True 
    for i in range(3,n):
        if n%2 == 0:
            return False
        if n%i == 0:
            return False
    return True
 
for j in range(1,101):
    if prime(j):
        print(j)


        


        