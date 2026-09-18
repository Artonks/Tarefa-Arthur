n = int(input('Digite um valor: '))

a = 0
b = 1

fibonacci = []

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print(" ".join(map(str, fibonacci)))