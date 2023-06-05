s=input()
v=input()
k=0
for i in range(len(s)):
    if s[i]==v:
        k=1
        print("True")
        print(i)
        break
if k==0:
    print("False")
