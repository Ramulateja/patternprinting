n=int(input())
for r in range(1,n+1):
    for c in range(1,n-r+1):#the star will print left by default the then we use spaces to push to the right side.
        print("|",end=" ")#"|"consider it as a space to get idea how spacing loop works.
    for c in range(1,2*r):
        print("*",end=" ")
    print()