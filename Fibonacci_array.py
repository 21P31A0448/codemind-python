n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(2,n-1):
    if a[i]==a[i-1]+a[i-2]:
        c+=1
if c==n-3:
    print("yes")
else:
    print("no")