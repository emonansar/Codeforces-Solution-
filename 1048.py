#1048
x=float(input())
if(x>=0 and x<=400):
    ns=x+x*.15
    r=ns-x
    p=15
elif(x>400 and x<=800):
    ns=x+x*.12
    r=ns-x
    p=12
elif(x>800 and x<=1200):
    ns=x+x*.10
    r=ns-x
    p=10
elif(x>1200 and x<=2000):
    ns=x+x*.07
    r=ns-x
    p=7
elif(x>2000):
    ns=x+x*.04
    r=ns-x
    p=4
print("Novo salario: %.2f" % ns)
print("Reajuste ganho: %.2f" % r)
print("Em percentual: %d" %p,"%")