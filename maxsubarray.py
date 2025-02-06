
#find subarrays

def find_subarrays(arr):
    n = len(arr)
    subarrays = []  

    for start in range(n): 
        for end in range(start, n):  
            subarrays.append(arr[start:end+1]) 

    return subarrays

arr = [1, 2, 3]
print("All Subarrays:", find_subarrays(arr))


# sum of subarray   


def maximum_subarray(arr):
  currentsum = []
  n = len(arr)
  for i in range(n):
    sum_of_no = 0
    for j in range(i,n):
      sum_of_no= sum_of_no + arr[j]
      currentsum.append(sum_of_no)
  maximum = max(currentsum)
  return maximum
arr = [5, -8, 3, 5, 6]
print(maximum_subarray(arr))


# Kadane's Algorithm    


def max_subarray(num):
  maximum = 0
  current_sum = 0
  for i in num:
    current_sum = current_sum +i
    maximum = max(maximum,current_sum)
    if current_sum < 0:  
            current_sum = 0
          
  return maximum
num = [5, -8, 3, 6, 7, -1]  
print(max_subarray(num))
