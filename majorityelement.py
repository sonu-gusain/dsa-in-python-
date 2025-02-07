#           mejority element  


# hashmap method 

def hashmap_mathod(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] = freq[i]+1
        else:
            freq[i]=1
        if freq[i] > len(nums)//2:
            return i
nums = [3, 3, 4, 2, 3, 3, 3]
print(hashmap_mathod(nums))
            


# Moore’s Voting Algorithm

def mejority_element(num):
    number = None
    count = 0
    for i in num:
        if count ==0 :
            number = i
        if i == number:
            count = count +1
        else:
            count = count -1

    return number
num = [3, 3, 4, 2, 3, 3, 3]
print(mejority_element(num))