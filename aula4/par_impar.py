import random

print("=== PAR ou ÍMPAR ===")

# Escolha do jogador
escolha = input("Você quer PAR ou ÍMPAR? ").strip().lower()
jogador_num = int(input("Escolha um número de 0 a 5: "))

# Computador gera um número aleatório
computador_num = random.randint(0, 5)

soma = jogador_num + computador_num
print(f"Você jogou {jogador_num}, computador jogou {computador_num}. Soma = {soma}")

# Descobrir se a soma é par ou ímpar
if soma % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

# Verificar o vencedor
if escolha == resultado.lower():
    print("Você venceu!")
else:
    print("O computador venceu!")
