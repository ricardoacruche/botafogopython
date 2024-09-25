# Solicita a distância a percorrer e a velocidade média
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))

# Calcula o tempo de viagem
tempo_viagem = distancia / velocidade_media

# Exibe o tempo de viagem em horas
print(f"O tempo estimado de viagem é de {tempo_viagem:} horas.")
