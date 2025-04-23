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