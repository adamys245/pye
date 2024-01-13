print('-__-'*20)
distancia = float(input('qual é a distancia da sua viagem?: '))
print('-__-'*20)
longa = 0.45 * distancia
curta = 0.50 * distancia

if distancia >= 200:
    print('hmmm, viagem longa ne. sua viagem custaram R${:.2f}'.format(longa))
    print('-__-'*20)
else:
    print('sua viagem é curta, então custara R${:.2f}'.format(curta))
    print('-__-'*20)