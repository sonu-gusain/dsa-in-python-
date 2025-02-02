
# binary to decimal (nagative)

def binary_to_decimal(num):

    decimal= 0

    m = str(num)
    is_negative = m[0] == '1' and len(m) in [8, 16, 32]
     
    n= len(m)
    
    for i in range(n):
        digit = int(m[i])
        power = n - 1 -i
        decimal = decimal + (digit*(2**power))
    
    
    if is_negative is True:
        decimal = decimal - 2**n
        return decimal
    else:
        return decimal

print(binary_to_decimal("10101110"))
