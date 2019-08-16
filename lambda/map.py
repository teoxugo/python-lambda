sequencia = [int(x) for x in input("Insira os números: ").split()]

print(list(map(lambda x: "par" if (x%2 == 0) else "impar",sequencia)))
