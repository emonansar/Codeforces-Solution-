a,b,c=map(float,input().split())
if(a>=b):
    if(a>=c):
        d=a;
        #print(maxx)
        if(b>=c):
            e=b
            f=c
        else:
            e=c
            f=b
    else:
        e=a
        if(b>=c):
            d=b
            f=c
        else:
            d=c
            f=b
else:
    if(b>=c):
        d=b
        if(a>=c):
            e=a
            f=c
        else:
            e=c
            f=a
    else:
        e=b
        if(a>=c):
            d=a
            f=c
        else:
            d=c
            f=a
#print('%f %f %f'% (d,e,f))
if(d>=e+f):
    print('NAO FORMA TRIANGULO')
else:
    if(d*d==e*e+f*f):
        print('TRIANGULO RETANGULO')
    if(d*d>e*e+f*f):
        print('TRIANGULO OBTUSANGULO')
    if(d**2<e**2+f**2):
        print('TRIANGULO ACUTANGULO')
    if(d==e and e==f):
        print('TRIANGULO EQUILATERO')
    if(d==e and d!=f) or (e==f and e!=d):
        print('TRIANGULO ISOSCELES')