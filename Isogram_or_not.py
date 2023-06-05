def solve(s):
    char_list=[]
    for char in s:
        if char.isalpha():
            if char in char_list:
                return False
            else:
                char_list.append(char)
    return True
s=input()
print(solve(s))