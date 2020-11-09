#1064
c=0
sum=0
for i in range(1,7):
    x=float(input())
    if(x>0):
        c=c+1
        sum=sum+x
print('%d valores positivos' % c)
print('%.1f' % (sum/c))