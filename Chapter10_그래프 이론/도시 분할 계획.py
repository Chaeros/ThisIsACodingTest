n,m=map(int,input().split())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

graph=[]
for i in range(m):
    a,b,cost=map(int,input().split())
    graph.append((cost,a,b))

graph.sort()

print(graph)

result=0
last=0
for i in graph:
    if find_parent(parent,i[1])!=find_parent(parent,i[2]):
        union_parent(parent,i[1],i[2])
        result+=i[0]
        last=i[0]

print(result-last)
 #   if find_parent(parent,a)!=find_parent(parent,b):
 #       union_parent(parent,a,b)
 #       graph.append(cost,a,b)
