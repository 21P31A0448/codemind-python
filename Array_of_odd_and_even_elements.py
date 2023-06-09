n=int(input())
a=list(map(int,input().split()))
p=[]
q=[]
for i in a:
    if i%2==1:
        p.append(i)
    else:
        q.append(i)
print(*p,*q,end=' ')