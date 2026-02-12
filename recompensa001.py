<<<<<<< HEAD
from datetime import date

hoje = date.today().strftime('%d/%m/%Y')

try:
    score = int(input('Digite seu score da semana: '))

    if score == 5:
        resultado = 'Recompensa máxima'
    elif score >= 3:
        resultado = 'Recompensa parcial'
    elif score >= 1:
        resultado = 'Sem recompensa'
    else:
        resultado = 'Reset necessário'

    print(resultado)

    with open('historico_hard.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{hoje} | Score: {score} | {resultado}\n')

except ValueError:
    print('Erro: digite apenas números inteiros')
=======
score=int(input('Digite seu score:'))
if score ==5:
    print('Semana perfeita! Recompensa máxima liberada!')
elif score >=3:
    print('Boa semana! Recompensa parcial liberada!')
elif score >=1:
    print('Semana fraca! Sem recompensa!')
else:
    print('Semana falha! Reset necessário!!!')
    
>>>>>>> 194469245e230180e2449026bd397adae1d0a176
