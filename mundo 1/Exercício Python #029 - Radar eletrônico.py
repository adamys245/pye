from colorama import Style,Fore

velo=int(input("Qual foi a velocidade?: "))
if velo <=80:
    print (Fore.BLUE+"A velocidade está dentro do limite!")
    print(Style.RESET_ALL)
else:
    print(Fore.RED+"Você ultrapassou a velocidade permitida de 80KM/h e pegou uma multa de R$280.00 ")
    print(Style.RESET_ALL)