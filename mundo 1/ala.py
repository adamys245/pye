#localidades
aonde=str(input("Aonde você mora?").strip().lower())
viagem=str(input("aonde você irá viajar?").strip().lower())

#Regiões/listas
norte=["amazonas","roraima","amapá","acre","rondônia"]

nordeste=["alagoas", "bahia", "ceará", "maranhão", "paraíba", "pernambuco", "piauí", "rio Grande do Norte","sergipe"]
centro_oeste=["mato grosso","góias","mato grosso do sul"]

for estado in norte:
    if viagem == estado:
        print("O valor é R$1.000")

    for estado2 in nordeste:
        if viagem == estado2:
            print("O valor é R$1.000")
