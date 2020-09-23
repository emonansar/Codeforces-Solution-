#1019
x=int(input())
h=x/3600
x=x%3600
m=x/60
x=x%60
print('%d:%d:%d' % (h,m,x))