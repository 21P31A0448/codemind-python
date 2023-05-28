n=int(input())
a=list(map(int,input().split()))
b=set(a)
s=0
for i in b:
    if i%2==0 and i!=0:
        s+=i
print(s)