#1. Faça um programa que leia um número não conhecido de valores correspondendo à quantidade de produtos e valor unitário do mesmo, contando a quantidade e somando o valor parcial da compra, até que seja informado a quantidade 0 (zero). Ao final, escreva a quantidade de itens comprados e o valor total da compra.

valorT = 0
cont = 0
while True :
    quant = float(input("Informe a quantidade do produto: "))
    if quant == 0 :
        break
    elif quant >= 1:
        valor = float(input("Informe o valor do produto: "))
        valorT = valorT + (quant * valor)
        cont = cont + 1
print("Quantidade de itens: %.0f"% cont)
print("Valor total da compra: R$%.2f"% valorT)
