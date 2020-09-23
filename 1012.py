#1012
pi = 3.14159
a,b,c=map(float,input().split())
tarea=0.5*a*c
carea=pi*c*c
trap=0.5*(a+b)*c
sqr=b*b
rec=a*b
print("TRIANGULO: %.3f" % tarea)
print("CIRCULO: %.3f" % carea)
print("TRAPEZIO: %.3f" % trap)
print("QUADRADO: %.3f" % sqr)
print("RETANGULO: %.3f" % rec)