#1101
while(1):
    sum=0
    a,b=map(int,input().split())
    if(a<=0 or b<=0):
        break
    else:
        if(a<b):
            a,b=b,a
        for i in range(b,a+1):
            print(i,end=" ")
            sum=sum+i
        print('Sum=%d'%sum,end="")
        print()