
<<<<<<< HEAD
#inverted  trangle pattern
# 1111
#  222
#   33
#    4

for i in range(1,5):
    for j in range(i-1):
     print("",end ="")
        
    for k in range(5-i):
        print(i,end="")

#peramid trangle 
#    1
#   121
#  12321
# 1234321
=======

>>>>>>> hollowpattern

#hollow dimand pattern

<<<<<<< HEAD
    for k in range(1,i+1):
        print(k,end="")
    for j in range(i-1,0,-1):
        print(j,end="")

=======
#   *
#  * *
# *   *
#  * *
#   *

for i in range(1,6,2):
    for j in range((6-i-1)//2):
        print(" ",end="")
    for j in range(i):
        if j==0 or j ==i-1:
            print("*",end="")
        else:
            print(" ",end="")
>>>>>>> hollowpattern
    print()

for i in range(3,0,-2):
    for j in range((6-i-1)//2):
        print(" ",end="")
    for j in range(i):
        if j==0 or j ==i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print() 

