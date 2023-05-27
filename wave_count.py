n=int(input())
arr=list(map(int,input().split()))
y=0
count=0
for i in range(0,n-2,2):
    if(arr[i]<arr[i+1]) and (arr[i+1]>arr[i+2]):
        y=1
        count+=1
    elif arr[i]>arr[i+1]:
        y=0
        break
if y==0:
    print("-1")
else:
    print(count)