a=input().split()
for i in a:
    c=[]
    d=[]
    for j in i:
        if j.isalpha():
            c.append(j)
    c.sort()
    k=0
    for d in range(len(i)):
        if i[d].isalpha():
            print(c[k],end='')
            k+=1
        else:
            print(i[d],end='')
    print(end=' ')