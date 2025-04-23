div = 1000
jur = 0.01
cont = 0
while div < 2000 :
    div = div + (div*jur)
    cont = cont + 1
print("Meses: %d"%cont)