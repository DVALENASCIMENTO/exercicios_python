#Implementar um script em python que imprima todos os números entre 1 e 50.
# Ao final, o programa também deve imprimir o somatório destes números.
# Este exercício deve ser implementado utilizando o comando while.
# Autor: Diego Vale do Nascimento - 09/10/2022
n = 50
i = 1
soma = 0

while(i <= n):
    if(i % 1 == 0):
        print('{} '.format(i), end='')
    soma += i
    i += 1

print(' - O Somatório destes números é: {}'.format(soma))


