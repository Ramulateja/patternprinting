n=int(input())
for r in range(0,n):#step 1 :no.of rows we want.
    for c in range(0,n):#no.of columns we want.
#it has to be inside the inner loop because whenever the r=1 started it enters into the c loop then it prints or execute the whatever it having inside of it no.of times as we mentioned. 
        print("*",end=" ")#the "end="" " helps us to prints the *'s side by side.  
    print()#it moved to next row after moving to next iteration.