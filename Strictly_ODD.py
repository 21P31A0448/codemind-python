n=int(input())
l=list(map(int,input().split()))
for i in range(1,n,2):
    if l[i]%2!=0:
        continue
    print(False)
    break
   
else:
    print(True)