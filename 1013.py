#1013
a,b,c=map(int,input().split())
large= (a+b+abs(a-b))/2
larger= (large+c+abs(large-c))/2
print("%d eh o maior" % larger)