def isPalin(word):
    if word.lower()==word.lower()[::-1]:
        return True
    else:
        return False
def countofPalin(str):
    count=0
    listofwords=str.split(" ")
    for elements in listofwords:
        if(isPalin(elements)):
            count+=1
    return(count)
str=input()
print(countofPalin(str))