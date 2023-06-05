r,c=map(int,input().split())
mat=[list(map(int,input().split()))for i in range(r)]
mx=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    mx.append(s)
print(max(mx))