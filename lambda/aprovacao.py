m1 = int(input())
m2 = int(input())                               m3 = int(input())                               

z = int((lambda m1, m2, m3 : (m1 + m2 + m3)/3)(m1,m2,m3))
if z < 6:
    print("Reprovado")
else:
    print("Aprovado")
