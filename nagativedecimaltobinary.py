
def decimal_to_binary(num):
    num = abs(num)
    if num==0:
        return 0
    binary = []
    
    while num>0:
        remainder = num%2
        binary.append(remainder)
        num=num//2
    binary.append(0)
    binary.reverse()

    compliment = []
    for j in binary:
        if j == 0:
            compliment.append(1)
        else:
            compliment.append(0)
    
    carry = 1
    for i in range(len(compliment) - 1, -1, -1):
            if compliment[i] == 1 and carry == 1:
                compliment[i] = 0
            elif compliment[i] == 0 and carry == 1:
                compliment[i] = 1
                carry = 0
    return compliment
print(decimal_to_binary(-8))