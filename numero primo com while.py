#Construir um programa que leia um número inteiro e positivo informado pelo usuário.
# O programa deve verificar se o número informado pelo usuário é primo ou não.
# Autor: Diego Vale do Nascimento - 09/10/2022

n = int(input("Insira um número par: "))
i = 2
primo = 0
while i < n and primo == 0:
    if n % i == 0:
        primo=1
        print('Não é primo!')
    i = i + 1
if primo == 0:
    print('É primo!')


