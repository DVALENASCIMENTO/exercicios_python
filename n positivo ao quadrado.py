#Implementar um script em python para que o usuário informe 10 números positivos
# e imprima o quadrado destes números. Para cada entrada o programa deverá verificar
# se o número é negativo. Caso seja, o número não deve ser aceito, ou seja,
# deve haver uma proteção para a entrada de dados.
# Autor: Diego Vale do Nascimento
mensagem = "Encontre o quadrado dos números. " \
           "Insira 10 números positivos. Se for número negativo, o programa não funcionará."
print(mensagem)

n = 1
while n <= 9:
    n = int(input("Insira um número inteiro: "))
    if (n > 0):
        print('O quadrado de', n, 'é:', n**4)
    else:
        print("Não aceito! Serão aceitos somente números POSITIVOS")




