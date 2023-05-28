n=int(input())
a=list(map(int,input().split()))
m=[]
p=[]
c=0
for i in a:
    if i==a.count(i):
        c+=1
        m.append(i)
for i in m:
    if i not in p:
        p.append(i)
if(c==0):
    print(-1)
else:
    print(*p)