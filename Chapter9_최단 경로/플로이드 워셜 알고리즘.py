INF=int(1e9)

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#각 간선 정보 입력받아 초기화
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

#플로이드 워셜 알고리즘 수행, 특정 노드 방문한 것과 현재 거리 비교하여 더 작은 비용의 간선 선택
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b],end=' ')
    print()