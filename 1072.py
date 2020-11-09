#1072
c=0
d=0
n=int(input())
for i in range(1,n+1):
    x=int(input())
    if(x>=10 and x<=20):
        c+=1
    else:
        d+=1
print('%d in'%c)
print('%d out'%d)