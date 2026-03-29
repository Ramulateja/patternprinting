n=int(input())
for r in range(1,n+1):
#i am given the start from ex:4 as n and end is row value then step -1.
#if row start from 0 then r=0 stop value means untill 1 it prints by removing 1.
#step1:  r=0 then start from example:4 to 0 and step is -1 means 4,3,2,1.
#step2:  r=1 then start from example:4 to 1 and step is -1 means 4,3,2.
#step2:  r=2 then start from example:4 to 2 and step is -1 means 4,3.
#step2:  r=3 then start from example:4 to 3 and step is -1 means 4.
    for c in range(n,r-1,-1):
        print("*",end=" ")
    print()