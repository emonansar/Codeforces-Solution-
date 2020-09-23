#1021
n=float(input())
n=n*100
a=n/10000
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % a)
n=n%10000
a=n/5000
print("%d nota(s) de R$ 50.00" % a)
n=n%5000
a=n/2000
print("%d nota(s) de R$ 20.00" % a)
n=n%2000
a=n/1000
print("%d nota(s) de R$ 10.00" % a)
n=n%1000
a=n/500
print("%d nota(s) de R$ 5.00" % a)
n=n%500
a=n/200
print("%d nota(s) de R$ 2.00" % a)
print("MOEDAS:")
n=n%200
a=n/100
print("%d moeda(s) de R$ 1.00" % a)
n=n%100
a=n/50
print("%d moeda(s) de R$ 0.50" % a)
n=n%50
a=n/25
print("%d moeda(s) de R$ 0.25" % a)
n=n%25
a=n/10
print("%d moeda(s) de R$ 0.10" % a)
n=n%10
a=n/5
print("%d moeda(s) de R$ 0.05" % a)
n=n%5
a=n/1
print("%d moeda(s) de R$ 0.01" % a)