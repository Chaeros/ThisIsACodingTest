array=[7,5,9,0,3,1,6,2,4,8]
print("변경 전: ",array)

for i in range(len(array)):
    min=array[i]
    for j in range(i+1,len(array)):
        if min>array[j]:
            tmp=array[j]
            array[j]=min
            array[i]=tmp
            min=tmp

print("변경 후: ",array)
