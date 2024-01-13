from random import randint
from colorama import Fore,Style

ad=(randint(1,4))

print (Fore.BLUE+"-_"*50)
print (Style.RESET_ALL)
print("estou pensando um numero de 1 a 4: ")
print (Fore.BLUE+"-_"*50)
print(Style.RESET_ALL)

esc=int(input("Adivinhe: "))

if esc==ad:
    print (Fore.BLUE+f"Foi o número {ad}, acertou!!!!")
    print (Style.RESET_ALL)
else:
    print(Fore.RED+f"Foi o número {ad}, errou:(")
    print (Style.RESET_ALL)
