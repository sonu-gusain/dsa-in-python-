
#hollow dimand pattern

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
