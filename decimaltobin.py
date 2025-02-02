# covert to decimal to binary

def decimal_to_binary(num):
    if num==0:
        return 0
    binary = []
    
    while num>0:
        remainder = num%2
        binary.append(remainder)
        num=num//2
    binary.reverse()
    return binary
    
print(decimal_to_binary(25)) 
print(decimal_to_binary(10))  