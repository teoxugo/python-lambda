import math

x1, y1, z1 = [int(x) for x in input("Insira as segundas coordenadas ").split()]
x2, y2, z2 = [int(x) for x in input("Insira as primeiras coordenadas ").split()]

print((lambda x1, y1, z1, x2, y2, z2 : math.sqrt(pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2)))(x1,y1,z1,x2,y2,z2))
