n=int(input())
arr=list(map(int,input().split()))
y=0
if arr[0]<arr[1]:
    for i in range(0,n-1,2):
        if(arr[i]>arr[i+1]):
            y=1
            print("no")
            break
    if y==0:
        print("yes")
else:
    for i in range(0,n-1,2):
        if(arr[i]<arr[i+1]):
            y=1
            print("no")
            break
    if y==0:
        print("yes")
