#1043
a,b,c=map(float,input().split())
if(a>=b):
    if(a>=c):
        maxx=a
    else:
        maxx=c
else:
    if(b>=c):
        maxx=b
    else:
        maxx=c
add=a+b+c
add=add-maxx
if(add>maxx):
    per=a+b+c
    print('Perimetro = %.1f' % per)
else:
    area=0.5*(a+b)*c
    print('Area = %.1f'% area)