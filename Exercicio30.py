A=[]
M=[]
for i in range(2):
    A.append(int(input("Digite os números: ")))
X=int(input("Digite o numero para a multiplicação: "))
for j in range(2):
    M.append(A[j]*X)
print(A)
print("x",X)
print(M)