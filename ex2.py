#2. O pais A tem 1200000 habitantes e a taxa de crescimento da população é de 3% ao ano. O pais B tem 1500000 habitantes e a taxa de crescimento da população é de 2% ao ano. Faça um programa que calcule quantos anos são necessários para que o país A tenha mais população que o país B.
pA = 1200000
pB = 1500000
cont = 0
while pA < pB :
    pA = (pA * 1.03)
    pB = (pB * 1.02)
    cont = cont + 1
print("Anos passados: ", cont)
