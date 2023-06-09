n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in range(n):
    if a[i]<b or a[i]>c:
        print(a[i],end=' ')
        s+=1
if s==0:
    print("-1")