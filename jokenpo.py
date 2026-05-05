import random

print("=== PEDRA, PAPEL E TESOURA ===")

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha pedra, papel ou tesoura (ou 'sair'): ").lower()

    if jogador == "sair":
        print("Fim do jogo!")
        break

    if jogador not in opcoes:
        print("Opção inválida!")
        continue

    computador = random.choice(opcoes)

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

    print()
