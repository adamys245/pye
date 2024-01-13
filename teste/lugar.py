clima = str(input("O clima é de: "))
dinheiro= float(input("Quantos reais você?:$ "))
lugar= ""

if clima =="sol" or "nublado" and dinheiro<=300:
    lugar= "Ponta negra"
else:
    lugar= "Praça da cidade"
print ("vou à "+lugar)