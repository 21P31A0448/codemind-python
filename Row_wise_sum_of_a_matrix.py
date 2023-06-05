r,c=map(int,input().split())
mat=[list(map(int,input().split()))for i in range(r)]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    print(s,end=' ')