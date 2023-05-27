n=int(input())
arr=list(map(int,input().split()))
y=999
m=0
for i in range(n):
    if arr[i]<y:
        y=arr[i]
        m+=1
if m==n:
    print("yes")
else:
    print("no")