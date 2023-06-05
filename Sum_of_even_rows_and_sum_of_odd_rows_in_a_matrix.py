r,c=map(int,input().split())
m=[]
n=[]
for i in range(r):
    lst=list(map(int,input().split()))
    for j in lst:
        if i%2==0:
            n.append(j)
        else:
            m.append(j)
print(sum(n),sum(m))