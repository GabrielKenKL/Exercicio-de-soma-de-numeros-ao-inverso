#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

#algoritmo série inversa
#declarar
N = 0
soma = 0

N = int(input("Digite o número a ser realizado o cálculo de soma: "))
for i in range(1, N + 1):
    soma += i **-1

print("A soma equivale a" , soma)