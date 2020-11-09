#1071
summ=0
x=int(input())
y=int(input())
if(x<y):
    x,y=y,x
for i in range(y+1,x):
    if(i%2!=0):
        summ=summ+i
print(summ)