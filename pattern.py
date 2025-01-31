# def num(n):
#     sum = 0
#     for i in str(n):
#         sum = int(i) + sum
#     return sum

# def sumnum():
#     x =  num(143)
#     print(x)
# sumnum()


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
print(factorial(3))

def binomial(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(binomial(6,3))
