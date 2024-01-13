import time
n=int(input("Digite de um numero de 0-9999: "))

if n<0 or n>9999:
    print ("Numero inválido")
    print ("Sair")
    time.sleep(1800)
else:
    print("Resolvendo...")

    time.sleep(0.5)


num=str(n)

unidade= num[0:1]
dezena= num[1:2]
centena= num[2:3]
milhar= num[3:4]

print(f"unidade: {unidade}")
print (f"dezena: {dezena}")
print (f"centena: {centena}")
print  (f"Milhar: {milhar}")