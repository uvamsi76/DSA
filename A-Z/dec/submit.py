def ispossible(arr,c,mid):
    cnt=0
    last=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]-last>=mid):
            cnt+=1
            last=arr[i]
    return cnt>=c
def maxcows(arr,c):
    arr.sort()
    low=1
    high=max(arr)-min(arr)
    while(low<=high):
        mid=(low+high)//2
        st=ispossible(arr,c,mid)
        if(st):
            low=mid+1
        else:
            high=mid-1
    return high


for _ in range(int(input())):
    n,c=map(int,input().split(' '))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(maxcows(arr,c))