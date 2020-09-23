#1042
a,b,c= map(int,input().split())
x=a
y=b
z=c
if a<=b :
    if a<=c:
        print(a)
        if b<=c:
            print(b)
            print(c)
        else :
            print(c)
            print(b)
    else :
        print(c)
        print(a)
        print(b)
else :
    if a>=c:
        if b>=c:
            print(c)
            print(b)
            print(a)
        else:
            print(b)
            print(c)
            print(a)
    else :
        print(b)
        print(a)
        print(c)
print()
print(x)
print(y)
print(z)