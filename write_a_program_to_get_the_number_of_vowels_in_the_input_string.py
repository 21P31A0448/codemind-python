s=input()
v='aeiouAEIOU'
c=0
for i in range(0,len(s)):
    if s[i] in v:
        c+=1
print(c)