a, b, c = [int(x) for x in input("Insira os números: ").split()]

print((lambda a,b,c: (c if b < c else b) if a < b else (c if a < c else a))(a,b,c))
