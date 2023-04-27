row, column = map(int, input().split())

result=-1
for i in range(row):
    tmp=list(map(int,input().split()))
    if result<min(tmp):
        result=min(tmp)

print(result)