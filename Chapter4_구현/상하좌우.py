m=int(input())

travelRoute=list(input().split())
xPos=1
yPos=1

for i in travelRoute:
    if(i=='L'):
        if(xPos!=1):
            xPos-=1

    elif(i=='R'):
        if(xPos!=m):
            xPos+=1

    elif(i=='U'):
        if(yPos!=1):
            yPos-=1

    elif(i=='D'):
        if(yPos!=m):
            yPos+=1

print(yPos, xPos)


