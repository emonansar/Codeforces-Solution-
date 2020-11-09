#1051
n=float(input())
if(n<=2000):
    print('Isento')
else:
    if(n>2000 and n<=3000):
        n=n-2000
        s=n*.08
    if(n>3000 and n<=4500):
        n=n-3000
        s=n*.18+1000*.08
    if(n>4500):
        n=n-4500
        s=n*.28+1500*.18+1000*.08
    print('R$ %.2f' %s)