# 5. Faça um programa que calcule e escreva quantos meses são necessários para uma aplicação de R$ 1.000,00, com juros de 1% ao mês atingir R$ 2.000,00.
div = 1000
jur = 0.01
cont = 0
while div < 2000 :
    div = div + (div*jur)
    cont = cont + 1
print("Meses: %d"%cont)
