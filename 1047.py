#1047
a,b,c,d=map(int,input().split())
if(c>a and d>b):
    m=d-b
    h=c-a
elif(c<a and d>b):
    m=d-b
    h=24+(c-a)
elif(c<a and d<b):
    m=60+d-b
    c=c-1
    h=24+(c-a)
elif(c>a and d<b):
    d=60+d
    c=c-1
    m=d-b
    h=c-a
elif(c==a and d<b):
    d=60+d
    c=c-1
    m=d-b
    h=24+(c-a)
elif(c==a and d>b):
    m=d-b
    h=c-a
elif(c==a and d==b):
    m=d-b
    h=24+(c-a)
print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (h,m))