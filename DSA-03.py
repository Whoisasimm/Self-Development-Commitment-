n=[10,2,5,4,6]
t=12

i=0
j=len(n)-1
while i<j:
    c = n[i]+n[j]
    if c==t:
        print("found", c)
        break
    elif c<t:
        i+=1
    else:
        j-=1