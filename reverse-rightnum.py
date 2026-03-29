n=int(input())
for r in range(1,n+1):
#step1:  r=0 then start from example:4 to 0 and step is -1 means 4,3,2,1.
#step2:  r=1 then start from example:4 to 1 and step is -1 means 4,3,2.
#step2:  r=2 then start from example:4 to 2 and step is -1 means 4,3.
#step2:  r=3 then start from example:4 to 3 and step is -1 means 4.
    for c in range(n,r-1,-1):
        print(c,end=" ")
    print()