n=int(input())
for r in range(1,n+1):
    for c in range(1,n-r+1):
        print(" ",end=" ")
    for c in range(1,2*r):
        print("*",end=" ")
    print()
for r in range(2,n+1):#we start it from 2 because the star middle part printed twise with 9 stars so to remove that i was started it from 2 to n rows.
    for c in range(r-1):
        print(" ",end=" ")
    for c in range(2*(n-r)+1):
        print("*",end=" ")
    print()