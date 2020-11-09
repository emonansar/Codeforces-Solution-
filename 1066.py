#1066
c=0
n=0
o=0
p=0
for i in range(1,6):
    x=int(input())
    if(x%2==0):
        c=c+1
    if(x>0):
        p+=1
    if(x<0):
        n+=1
    if(x%2!=0):
        o+=1
    i=i+1
print('%d valor(es) par(es)' %c)
print('%d valor(es) impar(es)' %o)
print('%d valor(es) positivo(s)' %p)
print('%d valor(es) negativo(s)' %n)