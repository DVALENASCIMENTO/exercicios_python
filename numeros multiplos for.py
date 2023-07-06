#Implemente um script em python que imprima todos os números múltiplos de 2 ou 3 em um intervalo
# definido pelo usuário. Este exercício deve ser implementado utilizando o comando for.
# Autor: Diego Vale do Nascimento - 09/10/2022

#M(3)={0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,...}.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
print('Os números múltiplos de 3 são: ')
for c in range(n1, n2):
    if (c)%3 == 0:
        print(c, end=' ')