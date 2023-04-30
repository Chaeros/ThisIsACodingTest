# 3600가지 경우의 수 중에서

num=int(input())
count=0

for i in range(num+1):
    for j in range(60):
        for k in range(60):
            time=str(i)+str(j)+str(k)
            if '3' in time:
                count+=1

print(count)