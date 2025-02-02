
def binary_to_decimal(num):
    decimal= 0

    m = str(num)
    n= len(m)

    for i in range(n):
        digit = int(m[i])
        power = n - 1 -i
        decimal = decimal + (digit*(2**power))
    return decimal
   


print(binary_to_decimal(11001))
