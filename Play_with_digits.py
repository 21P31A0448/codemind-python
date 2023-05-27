a=int(input())
s=list(map(int,input().split()))
g=0
for i in s:
    while(i):
        d=i%10
        g+=d
        i//=10
print(g)
    