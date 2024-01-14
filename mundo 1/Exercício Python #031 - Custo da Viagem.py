#localidades
aonde=str(input("Aonde você mora?").strip().lower())
viagem=str(input("aonde você irá viajar?").strip().lower())

#Regiões/listas
norte=["amazonas","roraima","amapá","acre","rondônia"]

nordeste= ["alagoas", "bahia", "ceará", "maranhão", "paraíba", "pernambuco", "piauí", "rio Grande do Norte","sergipe"]
# centro_oeste=["mato grosso","góias","mato grosso do sul"]

if aonde==(norte) or viagem==(nordeste):
    print("O valor é R$1.000")