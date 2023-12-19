# Inicializando um vetor para armazenar os votos
votos = [0] * 7  # Índices de 1 a 6 representam as opções, e o índice 0 não é utilizado

# Função para calcular o percentual
def calcular_percentual(votos_opcao, total_votos):
    return (votos_opcao / total_votos) * 100 if total_votos > 0 else 0

# Loop para receber votos
while True:
    try:
        voto = int(input("Digite o número correspondente ao Sistema Operacional (1 a 6, 0 para encerrar): "))
        
        if voto == 0:
            break

        if 1 <= voto <= 6:
            votos[voto] += 1
        else:
            print("Número inválido. Por favor, digite um número entre 1 e 6.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Calculando o total de votos
total_votos = sum(votos)

# Imprimindo resultados
print("\nSistema Operacional        Votos   %")
print("------------------------   -----   ---")

for i in range(1, 7):
    percentual = calcular_percentual(votos[i], total_votos)
    sistema_operacional = (
        'Windows Server' if i == 1 else
        'Unix' if i == 2 else
        'Linux' if i == 3 else
        'Netware' if i == 4 else
        'Mac OS' if i == 5 else
        'Outro'
    )
    # Ajustando a formatação para alinhar os valores
    print(f"{i}- {sistema_operacional:<26}{votos[i]:<7}{percentual:.0f}%")

# Imprimindo o total
print("------------------------   -----   ---")
print(f"Total\t\t\t    {total_votos}")

# Encontrando o Sistema Operacional mais votado
if total_votos > 0:
    indice_vencedor = votos.index(max(votos))
    percentual_vencedor = calcular_percentual(votos[indice_vencedor], total_votos)
    sistema_vencedor = (
        '' if indice_vencedor == 1 else
        'Unix' if indice_vencedor == 2 else
        'Linux' if indice_vencedor == 3 else
        'Netware' if indice_vencedor == 4 else
        'Mac OS' if indice_vencedor == 5 else
        'Outro'
    )
    # Ajustando a formatação para alinhar os valores
    print(f"\nO Sistema Operacional mais votado foi o {sistema_vencedor:<26}, com {votos[indice_vencedor]:<7}votos, correspondendo a {percentual_vencedor:.0f}% dos votos.")
else:
    print("\nNão houve votos registrados.")
