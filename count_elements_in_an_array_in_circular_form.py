n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(1,n-1):
    if(a[i-1])%2==0 and  (a[i+1])%2==1:
        c.append(i)
    elif(a[i-1])%2==1 and (a[i+1])%2==0:
        c.append(i)
if(a[n-2])%2==0 and (a[0])%2==1:
    c.append(i)
elif(a[n-2])%2==1 and (a[0])%2==0:
    c.append(i)
if(a[n-1])%2==0  and (a[1])%2==1:
    c.append(i)
elif(a[n-1])%2==1 and (a[1])%2==0:
    c.append(i)
print(len(c))