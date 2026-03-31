# n=int(input())
n=5
for r in range(1,n+1):
    for c in range(r-1):#the star will print left by default the then we use spaces to push to the right side.
        print("|",end=" ")#"|"consider it as a space to get idea how spacing loop works.
    for c in range(2*(n-r)+1):#now to print the stars from high to low we use the this because n=5 we have to get the 5 rows from 9 to 1 logic 1,3,5,7,9 we start if n=5 then we take odd num from 1 to untill we get wanted no.of values.
        print("*",end=" ")
    print()