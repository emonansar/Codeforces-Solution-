#1074
n=int(input())
for i in range(1,n+1):
    x=int(input())
    if(x==0):
        print('NULL')
    if(x%2==0 and x>0):
        print('EVEN POSITIVE')
    elif(x%2==0 and x<0):
        print('EVEN NEGATIVE')
    elif(x%2!=0 and x>0):
        print('ODD POSITIVE')
    elif(x%2!=0 and x<0):
        print('ODD NEGATIVE')