print('=== FECHAMENTO SEMANAL HARD ===\n')

try:
    with open('historico_hard.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        if not linhas:
            print('Nenhum registro encontrado.')
        else:
            print('Últimos registros:\n')
            for linha in linhas[-4:]:
                print(linha.strip())

except FileNotFoundError:
    print('Arquivo de histórico não encontrado.')
