n=int(input())
c=[]
k=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(k)):
    if(k[i]<a or k[i]>b):
        c.append(k[i])
#print(c)
if(len(c)>=2):
    print(min(c))
else:
    print(-1)