
# find uniqe no. use of  xor

def find_unique(arr):
    unique = 0
    for num in arr:
        unique ^= num  # XOR each number
    return unique

arr = [1, 2, 3, 2, 1]
print(find_unique(arr))




# find missing no. use of xor 

def find_missing(arr, n):
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i  # XOR all numbers from 1 to N

    for num in arr:
        xor_arr ^= num  # XOR all numbers in array

    return xor_all ^ xor_arr  # Missing number

arr = [1, 2, 4, 5]  
n = 5
print(find_missing(arr, n))



# swap the element use xor 

def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
print(swap(10,15))