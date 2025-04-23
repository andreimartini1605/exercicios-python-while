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