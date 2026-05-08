import random
import json

name = input("Digite seu nome: ")

"""Gera dois números aleatórios e solicitando a resposta do usuário"""

while True:
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    while True:
        try:
            response_user = int(input(f"Quanto é  {number_1} + {number_2}? "))
            break
        except ValueError:
            print("ERRO. Digite um número inteiro.")

    if response_user == number_1 + number_2:
        print("Parabéns, você acertou!")
    else:
        print("Resposta errada, tente novamente!")

    """Convertendo os Dados para Json"""

    data_for_round = {
        "nome do jogador": name,
        "conta": f"{number_1} + {number_2}",
        f"{name}": response_user,
        "resposta_correta": number_1 + number_2
    }

    try:
        with open('resultados.json', 'r', encoding='utf-8') as arquivo:
            historico = json.load(arquivo)
            if not isinstance(historico, list):
                historico = []
    except (FileNotFoundError, json.JSONDecodeError):
        historico = []

    historico.append(data_for_round)

    with open('resultados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)

    cont = input("Deseja continuar jogando? (s/n): ").strip().lower()
    if cont not in ("s", "sim", "y", "yes"):
        break