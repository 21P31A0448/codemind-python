r,c=map(int,input().split())
m=[]
m1=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
    m1.append(sum(l))
for i in range(c):
    s=0
    for j in range(r):
        s=s+m[j][i]
    m1.append(s)
print(max(m1))