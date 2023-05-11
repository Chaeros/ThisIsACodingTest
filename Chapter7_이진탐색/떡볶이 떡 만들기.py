n,m=map(int,input().split())

array=list(map(int,input().split()))

start=0
end=max(array)
target=m

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in range(n):
        if array[i]>mid:
            sum+=(array[i]-mid)
    if sum>=target:
        start=mid+1
        result=mid
    elif sum<target:
        end=mid-1

if result==None:
    print("불가능")
else:
    print(result)