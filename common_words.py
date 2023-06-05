s1=input().lower().split()
s2=input().lower().split()
s=[]
for i in s1:
    if i in s2:
        s.append(i)
for i in s2:
    if i in s:
        print(i,end=' ')