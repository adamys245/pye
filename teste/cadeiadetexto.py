#frase
frase = str("Caramba uau")

#_____________________________________________________________________________

#pegue o caractere dentro da "variável" do 0 até 9 pulando de 4 em 4
print (frase[0:9:4])
#pegue o caractere dentro da "variável" do começo até o 9
print (frase[:9])
#pegue o caractere dentro da "var" do 9 até o final
print (frase[9:])
#pegue o caractere dentro da "var" 7 até o final pulando de 3 em 3
print(frase[7::3])
#_________________________________________________________________________________

#quantos caracteres tem na "var" e o que está denro dela
print (len(frase))
#conte dentro da "var" existe o caractere de valor 'a'
print (frase.count('a'))
#conte dentro da "var" existe o caractere de valor 'a' de 0 até 7
print (frase.count('a',0,7))
#__________________________________________________________________________________

#procure uma frase dentro do "var" e mostre aonde ele começou 
#-1 significa que ele nn achou/nao existe
print (frase.find("uau"))

#uau existe dentro do "var"?
print ("uau" in frase)

#°transformação
#substituia dentro do "var", "uau" para "quero gozar"
print (frase.replace('uau','quero gozar'))
#deixa a frase dentro da "var" em maiuscula
print (frase.upper())

#remove os espaços inuteis da "var" str
#frase.rstrip()    ele irá apagar somente da direita, podemos fazer isso em outros comandos
#frase.lstrip()    somente a esquerda
frase.strip()


#divide os espaços
frase.split()
#junta os espaços com '-' ou outro caractere
'-'.join(frase)