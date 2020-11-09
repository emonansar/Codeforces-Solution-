#1080
n=int(input())
s=0
for i in range(1,100):
    n=int(input())
    if(n>s):
        s=n
        c=i
print(s)
print(c+1)