n=int(input())
array_all=list(map(int,input().split()))

m=int(input())
array_parts=list(map(int,input().split()))

#이진탐색 전에 필요한 정렬
array_all.sort()

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return "yes"
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return "no"

for i in range(m):
    print(binary_search(array_all,array_parts[i],0,n-1),end=' ')