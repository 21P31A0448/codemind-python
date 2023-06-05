a=input().lower()
s=[]
for i in a:
    if i not in s and i!=" " and a.count(i)==1:
        s.append(i)
print(len(s))