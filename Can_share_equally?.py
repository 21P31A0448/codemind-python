a,b=map(int,input().split())
res=0
res=a-2*b
if(a==0 and b%2==0):
    print('YES')
elif(a==0 and b%2!=0):
    print('NO')
elif(res%2==0):
    print('YES')
else:
    print('NO')