n=int(input())
a=list(map(int,input().split()))
p=[]
q=[]
for i in a:
    if i%2==0:
        p.append(i)
    else:
        q.append(i)
print(*p,*q,end=' ')