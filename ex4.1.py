div = 1000
jur = 0.01
cont = 0
while cont < 50 :
    div = div + (div * jur)
    cont = cont + 1
print("Dívida: R$%.2f"%div)