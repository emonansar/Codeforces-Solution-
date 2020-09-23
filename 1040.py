#1040
a,b,c,d=map(float,input().split())
avg=(a*2+b*3+c*4+d*1)/10
print('Media: %.1f'% avg)
if(avg>=7.0):
    print('Aluno aprovado.')
elif(avg<5.0):
    print('Aluno reprovado.')
elif(avg>=5.0 and avg<=6.9):
    print('Aluno em exame.')
    e=float(input())
    print('Nota do exame: %.1f' % e)
    avg1=(avg+e)/2
    if(avg1>=5.0):
        print('Aluno aprovado.')
    elif(avg1<=4.9):
        print('Aluno reprovado.')
    print('Media final: %.1f' % avg1)