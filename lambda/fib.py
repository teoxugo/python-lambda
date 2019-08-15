n = int(input())

fib = (lambda x : 0 if x == 0 else 1 if x == 1 else fib(x-1)+fib(x-2))

print(fib(n)
