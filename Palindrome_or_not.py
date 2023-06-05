def isPalindrome(s):
    return s==s[::-1]
s=input()
s=s.lower()
res=isPalindrome(s)
if res:
    print("True")
else:
    print("False")