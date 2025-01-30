
#peramid trangle 
#    1
#   121
#  12321
# 1234321

for i in range(5):
    for j in range(5-i-1):
        print(" ",end ="")

    for k in range(1,i+1):
        print(k,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

