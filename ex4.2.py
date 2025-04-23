# 4. Faça um programa que calcule o valor final de uma dívida de R$ 1.000,00, com uma taxa de juros de 1% ao mês, após 50 meses. Faça um programa usando o while e o mesmo programa usando for.
div = 1000
jur = 0.01
cont = 0
for i in range (50) :
    div = div + (div * jur)
    cont = cont + 1
print("Dívida: R$%.2f"%div)
