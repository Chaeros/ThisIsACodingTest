n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for i in range(n+1)]
distance=[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split())

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[i][j],end=' ')
    print()

if graph[1][x]==INF or graph[x][k]==INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])