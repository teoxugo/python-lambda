x = input()
y = input()

true = lambda x, y: x
false = lambda x, y: y

dict = {'1': True,
        '0': False}

print((lambda x, y: not dict[y] if dict[x] else dict[y])(x,y))
