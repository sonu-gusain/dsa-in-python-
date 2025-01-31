
#binomial ...

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def binomial(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(binomial(6,3))
