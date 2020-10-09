a,b=map(int,input().split())
if a>=b:
    a=24-a
    a=a+b
else:
    a=b-a
print('O JOGO DUROU %d HORA(S)' %a) 