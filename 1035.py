#1035
a,b,c,d=map(int,input().split())
if(b>c and d>a and c>0 and d>0 and (a%2)==0 and (c+d)>(a+b)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')