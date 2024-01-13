from random import choice,randint

print('________________\033[1;36;44mGERADOR DE SENHA\033[m________________')
print('_'*50)
print('-'*50)
print('_'*50)
print('-'*50)
print('_'*50)



print('\033[4;0;0mescolha uma opção de senha\033[m')
print('_'*50)
print("""\033[1;32;42mescolha! 
opcao 1: letras e numero
opcao 2: letras e simbolos/str
opcao 3: numero e simbolos/str
opcao 4: apenas simbolos/str
opcao 5: apenas letras
opcao 6: apenas numeros\033[m""")
print('_'*50)
op = int(input('qual escolha sua opcao!: '))
#uma lista com todas str possivel gay?
print('_'*50)

l = ['w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m'
     ,'!','@','#','$','%','&','*','?','°','/','~','+','=','-','§','¹','²','³','£','¢','¬','ª','º','Q','W','E'
     ,'R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V','B','N','M']

lista = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B'
     ,'N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','k','l','z','x','c','v','b','n','m']
#cada um str aleatorio.
li = choice(lista)
li2 = choice(lista)
li3 = choice(lista)
li4 = choice(lista)
li5 = choice(lista)
li6 = choice(lista)
li7 = choice(lista)
li8 = choice(lista)
li9 = choice(lista)
li10 = choice(lista)
li11 = choice(lista)
li12 = choice(lista)
li13 = choice(lista)
li14 = choice(lista)

#str e simbolos

la = choice(l)
la2 = choice(l)
la3 = choice(l)
la4 = choice(l)
la5 = choice(l)
la6 = choice(l)
la7 = choice(l)
la8 = choice(l)
la9 = choice(l)
la10 = choice(l)
la11 = choice(l)
la12 = choice(l)
la13 = choice(l)
la14 = choice(l)

#cada um a funçao de fonecer um numnero aleatorio

n = randint(1,9)
n2 = randint(1,9)
n3 = randint(1,9)
n4 = randint(1,9)
n5 = randint(1,9)
n6 = randint(1,9)
n7 = randint(1,9)
n8 = randint(1,100)
n9 = randint(10,20)
n10 = randint(1,30)
n11 = randint(1,50)
n12 = randint(70,100)
n13 = randint(30,43)
n14 = randint(23,41)

if op == 1:
    print('SENHA: {}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(n,li2,n3,li4,n5,li6,n7,li8,n9,li10,n11,li12,n13,li14))
    # letras e numero
    print('_'*50)
    
elif op == 2:
     print('SENHA: {}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(li,la2,li3,la4,li5,la6,li7,la8,li9,la10,li11,la12,li13,la14))
     #letras e simbolos
     print('_'*50)

elif op == 3:
     print('SENHA: {}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(la,n2,la3,n4,la5,n6,la7,n8,la9,n10,la11,n12,la13,n14))
     #numero e simbolos
     print('_'*50)

elif op == 4: 
     print('{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(li,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14))
     #simbolos
     print('_'*50)


elif op == 5:
     print('SENHA: {}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(la,la2,la3,la4,la5,la6,la7,la8,la9,la10,la11,la12,la13,la14))
     # so palavras
     print('_'*50)


elif op == 6:
     print('SENHA: {}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(n,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14))
     #apenas numeros
print('_'*50)