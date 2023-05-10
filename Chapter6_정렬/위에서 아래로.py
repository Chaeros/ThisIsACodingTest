n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))
print("정렬 전: ",array)

array.sort()
array.reverse()
print("정렬 후: ",array)