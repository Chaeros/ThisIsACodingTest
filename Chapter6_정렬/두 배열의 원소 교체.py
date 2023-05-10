n,k=map(int,input().split())

A=[]
B=[]

A=list(map(int,input().split()))
B=list(map(int,input().split()))

#for i in range(n):
#    A.append(int(input()))

#for i in range(n):
#    B.append(int(input()))

print(A)
print(B)

A.sort()
B.sort()
print(A)
print(B)

for i in range(k):
    if A[i]<B[len(B)-1-i]:
        A[i],B[len(B)-1-i]=B[len(B)-1-i],A[i]

print(A)
print(B)

print(sum(A))