pA = 1200000
pB = 1500000
cont = 0
while pA < pB :
    pA = (pA * 1.03)
    pB = (pB * 1.02)
    cont = cont + 1
print("Anos passados: ", cont)