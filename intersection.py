

#intersection method of array 



arr = [5,4,6,7,8]
arr2= [1,4,9,7]
result = []
for i in arr:
    if i in arr2:
        if i not in result:
            result.append(i)
print(result)



arr = [5,4,6,7,8]
arr2= [1,4,9,7]
result = []
for num1 in arr: 
  for num2 in arr2: 
    if num1 == num2:  
      if num2 not in result:
        result.append(num1)
print(result)
    



arr = [5,4,6,7,8]
arr2= [1,4,9,7,5]
arr3= [2,4,1,7,5]
result = []
for num1 in arr:  
  for num2 in arr2:  
    for num3 in arr3:
      if num1 == num2 ==num3: 
        if num1 not in result:
          result.append(num1)
print(result)
