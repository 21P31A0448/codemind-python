n=list(map(str,input().split()))
a=[]
for i in n:
    a.append(abs(ord(min(i))-ord(max(i))))
for i in a:
    print(i,end=' ')