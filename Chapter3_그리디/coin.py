m=int(input())

c500=m//500
c100=(m-c500*500)//100
c50=(m-c500*500-c100*100)//50
c10=(m-c500*500-c100*100-c50*50)//10

print(c500,c100,c50,c10)

