from collections import deque

n,m=map(int,input().split())

queue =deque([[0,0]])

dx=[1,-1,0,0]
dy=[0,0,-1,1]

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
graph[0][0]=1

def bfs():
    while queue:
        v = queue.popleft()
        for i in range(4):
            x=v[0]+dx[i]
            y=v[1]+dy[i]
            if x>-1 and x<n and y>-1 and y<m:
                if graph[x][y]==1:
                    graph[x][y]+=graph[v[0]][v[1]]
                    queue.append([x,y])

bfs()
print(graph[n-1][m-1])