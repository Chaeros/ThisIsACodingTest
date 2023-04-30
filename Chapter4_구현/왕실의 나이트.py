val=input()

xPos=ord(val[0])
yPos=int(val[1])
count=0

#LLU
if(val[0]>='c' and yPos-2>=1):
    count+=1
    print("LLU")
#LLD
if(val[0]>='c' and yPos<=7):
    count+=1
    print("LLD")
#RRU
if(val[0]<='f' and yPos-2>=1):
    count+=1
    print("RRU")
#RRD
if(val[0]<='f' and yPos<=7):
    count+=1
    print("RRD")
#UUL
if(xPos-1>=ord('a') and yPos>=3):
    count+=1
    print("UUL")
#UUR
if(xPos+1<=ord('h') and yPos>=3):
    count+=1
    print("UUR")
#DDL
if(xPos-1>=ord('a') and yPos<=6):
    count+=1
    print("DDL")
#DDR
if(xPos+1<=ord('h') and yPos<=6):
    count+=1
    print("DDR")

print(count)