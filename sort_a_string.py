s=list(input())
b=[]
c=[]
for i in s:
    if i.isalnum():
        b.append(i)
b.sort()
j=0
for i in range(len(s)):
    if s[i].isalnum():
        s[i]=b[j]
        j+=1
print(''.join(s))