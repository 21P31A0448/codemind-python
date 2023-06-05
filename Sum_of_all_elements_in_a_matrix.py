r,c=map(int,input().split())
s=0
for i in range(r):
    lst=list(map(int,input().split()))
    for j in lst:
        s=s+j
print(s)