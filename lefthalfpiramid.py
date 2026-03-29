#in this program we print the left half piramid.
n=int(input())
for r in range(1,n+1):#The loop iterate from 1 to n.
#in this we have to print the stars at the end.
#first we print specific no.of spaces based on the row value.
#
    for c in range(1,n-r+1):#in this loop the range is 1 to  
        print(" ",end=" ")
    for c in range(r):
        print("*",end=" ")
    print()