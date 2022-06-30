m=1000
i=0
c=0
while i<=m :
    c=c+i*i*i*i*i*i
    if c <=100000:
        i+=1
    else:

        print(i,c)
        break

