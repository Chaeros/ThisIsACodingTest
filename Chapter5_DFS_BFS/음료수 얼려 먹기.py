n,m=map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(row,col):
    if graph[row][col]==0:
        graph[row][col]=1
        # 상
        if row-1>-1 :
            dfs(row-1,col)
        # 하
        if row+1<n:
            dfs(row+1,col)
        # 좌
        if col-1>-1:
            dfs(row,col-1)
        # 우
        if col+1<m:
            dfs(row,col+1)

count=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            count += 1
        dfs(i,j)

print(count)