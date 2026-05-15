import random
import json
import matplotlib.pyplot as plt

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

print("\nFim do Jogo")
print("Fazendo o gráfico dos jogadores...")

acertos = 0
erros = 0


for rodada in historico:
    if rodada.get("nome do jogador") == name:
        resposta_usuario = rodada.get(name)
        resposta_correta = rodada.get("resposta_correta")
        
        if resposta_usuario == resposta_correta:
            acertos += 1
        else:
            erros += 1

# Teste de biblioteca Matplotlib
categorias = ['Acertos', 'Erros']
quantidades = [acertos, erros]
cores = ['#4CAF50', '#F44336'] #Igual no minecraft quando criava uma textura.

plt.bar(categorias, quantidades, color=cores)
plt.title(f'Resultado de {name}')
plt.xlabel('Resultados')
plt.ylabel('Quantidade de Partidas')

import math
plt.yticks(range(0, max(quantidades) + 2))

#Imprime o gráfico
plt.show()