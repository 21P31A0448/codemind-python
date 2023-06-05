N,M=map(int,input().split())
a=[list(map(int,input().split()))for i in range(N)]
sum=0
for i in range(N):
    for j in range(M):
        if(i==0):
            sum+=a[i][j]
        elif(i==N-1):
            sum+=a[i][j]
        elif(j==0):
            sum+=a[i][j]
        elif(j==M-1):
            sum+=a[i][j]
print(sum)