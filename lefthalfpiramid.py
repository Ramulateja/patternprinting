#in this program we print the left half piramid.
n=int(input())
for r in range(1,n+1):#The loop iterate from 1 to n.
#in this we have to print the stars at the end.
#first we print specific no.of spaces based on the row value.
#steps:
#step 1: 1st line we print n-row spaces means if n=4 and r=1 and +1 because end value it doesn't take that's y we use +1 we need to give 3 spaces.  
#step 2: 1st line we print n-row spaces means if n=4 and r=2 and +1 because end value it doesn't take that's y we use +1 we need to give 2 spaces.  
#step 3: 1st line we print n-row spaces means if n=4 and r=3 and +1 because end value it doesn't take that's y we use +1 we need to give 1 spaces.  
#step 4: 1st line we print n-row spaces means if n=4 and r=4 and +1 because end value it doesn't take that's y we use +1 we need to give 0 spaces.  
    for c in range(1,n-r+1):# in this loop the range is 1 to ex:n=4 ,r=1 then 4-1 = 3 spaces.
        print(" ",end=" ")
    for c in range(1,r+1):
        print("*",end=" ")
    print()