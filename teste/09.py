print('\033[1;35m=\033[m'*50)
print('{:=^40}'.format(' \033[4;37m LOJA DO APOLO \033[m '))
print('\033[1;36m=\033[m'*50)
gasto = float(input('QUANTO VOÇE GASTOU?: '))
print('FORMA DE PARGAMENTO')
print('[1] AVISTA  EM DINHEIRO')
print('[2] AVISTA NO CARATÃO')
print('[3] 2x NO CARTÃO: SEM JUROS')
print('[4] 3x OU MAIS NO CARTÃO: COM 20% DE JUROS')
op = int(input('ESCOLHA: '))
print('\033[1;32m=\033[m'*50)
if op == 1:
    desconto = (10 / 100) * gasto
    desconto1 = gasto - desconto 
    print('VOCE ESCOLHEU EM AVISTA NO DINHEIRO EM E VOCE TERA 10% DE DESCONTO')
    print('de {:.2f} foi para {:.2f}!!!'.format(gasto, desconto1))
    print('\033[1;32m=\033[m'*50)
elif op == 2:
    desconto = (5 / 100) * gasto
    desconto1 = gasto - desconto
    print('VOCE ESCOLHEU EM AVISTA NO CARTÃO E TERA 5% DE DESCONTO ')
    print('DE {:.2f} VAI PARA {:.2f}'.format(gasto,desconto1))
    print('\033[1;32m=\033[m'*50)
elif op == 3:
    fatura = gasto / 2
    print('VOCE ESCOLHEU PAGAR NO CARTÃO EM 2X')
    print('VOCE TERA QUE PAGAR {:.2f} NA FATURA DO CARTÃO POR 2 MESES'.format(fatura))
    print('\033[1;32m=\033[m'*50)
elif op == 4:
    print('VOCE ESCOLHEU PAGAR NO CARTÃO VOCE PAGARAM EM QUANTAS VEZ?')
    vez = int(input('PAGARAM EM:'))
    print('\033[1;32m=\033[m'*50)
    dividi = (gasto / vez)
    juros =  (20 / 100) * dividi+dividi
    print('VOCE PAGARAM {} POR {} MESES NA FATURA DO SEU CARTÃO'.format(juros,vez))
    print('\033[1;32m=\033[m'*50)