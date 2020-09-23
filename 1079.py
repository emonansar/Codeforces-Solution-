#1079
n=int(input())
for i in range (n):
    a, b, c=map(float,input().split())
    avg=(2*a+3*b+5*c)/10
    print("%.1f" % avg)