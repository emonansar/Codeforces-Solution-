#1020
x=int(input())
y=x/365
x=x%365
m=x/30
x=x%30
print('%d ano(s)' % y)
print('%d mes(es)' % m)
print('%d dia(s)' % x)