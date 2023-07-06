#Construir um programa que leia um número inteiro e positivo informado pelo usuário.
# O programa deve verificar se o número informado pelo usuário é primo ou não.
# Autor: Diego Vale do Nascimento - 09/10/2022

n = int(input("Insira um número inteiro: "))
primos = []
for a in range(1, n + 1):
    if n % a == 0:
        primos.append(a)
    else:
        pass
if len(primos) == 2:
    print('É primo')
else:
    print('Não é primo')
