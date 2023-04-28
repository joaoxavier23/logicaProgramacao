n = int(input("Digite o tamanho das listas: "))
A = []
B = []
C = []
for x in range(n):
    A.append(int(input("Digite um número: ")))
for i in range(n):
    B.append(int(input("Digite um número para a segunda lista: ")))
for y in range(n):
    C.append(A[y] + B[y])
print(A)
print(B)
print(C)
