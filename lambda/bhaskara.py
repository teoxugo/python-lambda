import math

a = int(input())
b = int(input())
c = int(input())

delta = (lambda a, b, c: (b**2) - (4 * a * c))(a,b,c)
if (delta > 0 ):
    x1 = (lambda a,b,delta: (-b + math.sqrt(delta))/2*a)(a,b,delta)
    print("A primeira raiz é: {}".format(x1))

    x2 = (lambda a,b,delta: (-b - math.sqrt(delta))/2*a)(a,b,delta)
    print("A segunda raiz é: {}".format(x2))
else:
    print("Não existem raizes para essa equação")
