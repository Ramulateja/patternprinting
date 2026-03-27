n=int(input())
for r in range(0,n):#from 0 to n-1 not n because it doesn't take untill n.
    for c in range(0,r+1):#from 0 to r+1 means lets consider the n=4,it print 0 to r+1"value is 1 because row=1". 
        print("*",end=" ")
    print()