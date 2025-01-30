
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

for i in range(5):
    for j in range(5-i-1):
        print(" ",end ="")

    for k in range(1,i+1):
        print(k,end="")
    for j in range(i-1,0,-1):
        print(j,end="")

    print()

