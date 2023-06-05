s=input()
a='aeiouAEIOU'
f=0
for i in range(len(s)):
    if s[i] not in a and s[i]!=' ' and s[(len(s)-1)-i] in a:
        f+=1
print(f)