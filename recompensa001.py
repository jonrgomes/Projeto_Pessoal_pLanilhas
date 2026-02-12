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
