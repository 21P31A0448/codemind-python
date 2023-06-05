s=input().lower()
d=[]
for i in s:
    if s.count(i)==1 and i!=" ":
        d.append(i)
        d.sort()
for i in d:
    print(i,end='')