

def change(cost, amnt):
    a =b=c=d = amnt;twe=0;ten=0;fiv=0;two=0;one=0

    if amnt-cost >= 20:
        twe=int((amnt-cost)/20)
        amnt=(amnt-cost)%20
      
    if (min(a,cost+amnt))-cost >= 10:        
        ten=int((min(a,cost+amnt)-cost)/10)
        a=(min(a,cost+amnt)-cost)%10
        
    if (min(b,cost+a,cost+amnt))-cost >= 5:
        fiv=int((min(b,cost+a)-cost)/5)
        b=(min(b,cost+a)-cost)%5
    if (min(c,cost+b,cost+a,cost+amnt))-cost >= 2:
        two=int((min(c,cost+b)-cost)/2)
        c=(min(c,cost+b)-cost)%2
    if (min(d,cost+c,cost+b,cost+a,cost+amnt))-cost >= 1:
        one=1
           
    print("twenty:",twe,"ten:",ten,"five:",fiv,"two:",two,"one:",one)
        

cost, amnt = input().split()
cost=int(cost); amnt=int(amnt)
change(cost, amnt) 
