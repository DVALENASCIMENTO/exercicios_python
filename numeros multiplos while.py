#Implemente um script em python que imprima todos os números múltiplos de 2 ou 3 em um intervalo
# definido pelo usuário. Este exercício deve ser implementado utilizando o comando while.
# Autor: Diego Vale do Nascimento - 12/10/2022

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

while True:
    if(n1 * 3 < n2):
        print ('{} '.format(n1 * 3), end='')
        n1 += 1
    else:
        break