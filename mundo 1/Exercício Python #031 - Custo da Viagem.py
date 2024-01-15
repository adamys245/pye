#localidades
aonde=str(input("Aonde você mora?").strip().lower())
viagem=str(input("aonde você irá viajar?").strip().lower())

#Regiões/listas
norte=["amazonas","roraima","amapá","acre","rondônia","pará"]

nordeste=["alagoas", "bahia", "ceará", "maranhão", "paraíba", "pernambuco", "piauí", "rio Grande do Norte","sergipe"]
centro_oeste=["mato grosso","góias","mato grosso do sul"]
sudeste=["espirito santo","são paulo", "minas gerais", "rio de janeiro"]
sul= ["paraná", "santa catarina", "rio grande do sul"]
#mesmas regiões
if viagem in norte:
    if aonde in norte:
        print("O valor é R$1.000")
if viagem in nordeste:
    if aonde in nordeste:
        print("O valor é R$1.000")

if viagem in centro_oeste:
    if aonde in centro_oeste:
        print("O valor é R$1.000 ")
#regioes diferentes
        #-viagem para norte
        #nordeste para norte
if viagem in norte:
    if aonde in nordeste:
        print("O valor é R$2.000")
        #centro oeste para norte
if viagem in norte:
    if aonde in centro_oeste:
        print ("O valor é R$2.500")
    #sudeste para norte
if viagem in norte:
    if aonde in sudeste:
        print("O valor será R$3.000")
        #sul para norte
if viagem in norte:
    if aonde in sul:
        print("O valor será R$3.500")
        #_______________________________
            #nordeste
    #Viagem para nordeste
#norte para nordeste
if viagem in nordeste:
    if aonde in norte:
        print("O valor será R$1.500")
#sudeste para nordeste
if viagem in nordeste:
    if aonde in sudeste:
        print ("O preço será R$2.000")
        #sul para nordeste
if viagem in nordeste:
    if aonde in sul:
        print("O preço será R$2.000")
#centro oeste para nordeste
if viagem in nordeste:
    if aonde in centro_oeste:
        print("O valor será R$2.500")
#____________________________________________________
#centro oeste
        #norte para centro oeste
if viagem in centro_oeste:
    if aonde in norte:
        print("O preço será R$1.000")
        #nordeste para centro oeste
if viagem in centro_oeste:
    if aonde in nordeste:
        print("O preço será R$1.500")
        #sudeste para centro oeste
if viagem in centro_oeste:
    if aonde in sudeste:
        print("O preço será R$2.000")
        #sudeste para centro oeste
if viagem in centro_oeste:
    if aonde in sudeste:
        print("o preço será R$2.500")
        #sul para centro oeste
if viagem in centro_oeste:
    if aonde in sul:
        print("O preço será R$3.000")
#________________________________________
#sudeste

if viagem in sudeste:
    if aonde in norte:
        print("O preço será R$2.000")
if viagem in sudeste:
    if aonde in nordeste:
        print("O preço será R$1.500")
if viagem in sudeste:
    if aonde in centro_oeste:
        print("O preço será R$1.600")
if viagem in centro_oeste:
    if aonde in sul:
        print("O preço será R$1.700")
 #Sul
if viagem in sul:
    if aonde in norte:
        print("O preço será R$2.500")
if viagem in sul:
    if aonde in nordeste:
        print("O preço será R$2.000")
if viagem in sul:
    if aonde in centro_oeste:
        print("O preço será R$2.800")
if viagem in sul:
    if aonde in sudeste:
        print("O preço será R$2.500")

#Obrigado yakuu por ter me ajudado:)