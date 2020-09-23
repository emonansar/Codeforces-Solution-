#1010
a,b,c=map(float,input().split())
s1=b*c
d,e,f=map(float,input().split())
s2=e*f
s1=s1+s2
print("VALOR A PAGAR: R$ %.2f" % s1)