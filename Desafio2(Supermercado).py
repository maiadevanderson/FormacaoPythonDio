# Lê o número de casos de teste
T = int(input())

# Inicializa uma lista para armazenar os resultados
resultados = []

# Para cada caso de teste
for _ in range(T):
    # Lê os valores N (número de refrigerantes comprados) e K (número de garrafas vazias para ganhar uma cheia)
    N, K = map(int, input().split())

    # Calcula o número de garrafas cheias e garrafas vazias
    garrafas_cheias = N // K
    garrafas_vazias = N % K

    # Calcula o total de garrafas que o cliente terá no segundo dia
    total = garrafas_cheias + garrafas_vazias

    # Adiciona o resultado à lista de resultados
    resultados.append(total)

# Imprime os resultados para cada caso de teste
for resultado in resultados:
    print(resultado)
