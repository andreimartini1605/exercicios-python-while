# 3. A KXorro QuemT vende hotdog a R$ 10,00, Crepes a R$ 7,00 e refri a R$ 5,00. Faça um programa com um menu com as opções:
# 1 - Hotdog $10,00
# 2 - Crepes $ 7,00
# 3 - Refri R$ 5,00
# 9 - Finalizar venda
# Para cada opção 1, 2 ou 3, ler a quantidade e calcule o valor total da venda. Ao finalizar a venda, escrever o valor total da venda.
valor = 0
print("1- Cachorro Quente: R$10,00")
print("2- Crepes: R$7,00")
print("3- Refri: R$5,00")
print("9- Finalizar venda")
while True :
    cod = int(input("Digite o código do produto: "))
    if cod == 9 :
        break
    elif cod == 1 :
        quant = int(input("Digite a quantidade de cachorros quentes: "))
        valor = valor + (quant * 10)
    elif cod == 2 :
        quant = int(input("Digite a quantidade de crepes: "))
        valor = valor + (quant * 7)
    elif cod == 3 :
        quant = int(input("Digite a quantidade de refrigerantes: "))
        valor = valor + (quant * 5)
print("Valor total da compra: R$%.2f"%valor)
