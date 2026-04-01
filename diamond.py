n=int(input())
for r in range(1,n+1):
    for c in range(1,n-r+1):
        print(" ",end=" ")
    for c in range(1,2*r):
        print("*",end=" ")
    print()
for r in range(1,n+1):
    for c in range(r-1):
        print(" ",end=" ")
    for c in range(2*(n-r)+1):
        print("*",end=" ")
    print()