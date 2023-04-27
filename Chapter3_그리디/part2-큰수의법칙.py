n,m,k=map(int,input().split())
list=list(map(int,input().split()))

sum=0
list.sort()
biggestNum=list[n-1]
secondBiggestNum=list[n-2]

print(biggestNum,secondBiggestNum)

for i in range(m):
    if (i+1)%k==0 :
        sum+=secondBiggestNum
    else :
        sum+=biggestNum

print(sum)
