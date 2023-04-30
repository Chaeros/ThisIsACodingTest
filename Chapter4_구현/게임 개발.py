row,col=map(int,input().split())
x,y,direction=map(int,input().split())

mx=[-1,0,1,0]
my=[0,1,0,-1]

visited=[[0]*col for _ in range(row)]

# visited=[]
# tmp=[0]*col
# print(tmp)
# for i in range(row):
#     visited.append(tmp)
#     print(visited)

array=[]
for i in range(row):
    array.append(list(map(int,input().split())))

def rotate():
    global direction
    direction-=1
    if direction==-1:
        direction=3

visited[x][y]=1
count=1
rotate_count=0
while True:
    rotate()
    dx=x+mx[rotate_count]
    dy=y+my[rotate_count]
    if visited[dx][dy]==0 and array[dx][dy]==0:
        visited[dx][dy] = 1
        x=dx
        y=dy
        count+=1
        rotate_count=0
        continue
    else:
        rotate_count+=1

    if rotate_count==4:
        x-=mx[direction]
        y-=my[direction]
        if array[x][y]==1:
            break
        rotate_count=0

print(count)