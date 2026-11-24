# UC4 - DESENVOLVER ALGORITMOS
# DESAFIO 01 - O CAMPEONATO DE GAMES DA NINTENDO
# Entrada, validação, decisão e saída.

import math


def ler_inteiro(pergunta, minimo=0, maximo=None):
    while True:
        entrada = input(pergunta + ": ").strip()
        try:
            numero = int(entrada)
            if numero < minimo or (maximo is not None and numero > maximo):
                print("Erro: valor fora do intervalo permitido.")
                continue
            return numero
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def ler_decimal(pergunta, minimo=0, maximo=None):
    while True:
        entrada = input(pergunta + ": ").strip().replace(",", ".")
        try:
            numero = float(entrada)
            if not math.isfinite(numero) or numero < minimo or (maximo is not None and numero > maximo):
                print("Erro: valor fora do intervalo permitido.")
                continue
            return numero
        except ValueError:
            print("Erro: informe um número válido.")


def main():
    print("DESAFIO 01 — O Campeonato de Games da Nintendo")
    pontos = ler_inteiro("Pontuação do participante", 0)
    vitorias = ler_inteiro("Número de vitórias", 0)
    if pontos >= 500 and vitorias >= 3:
        mensagem = "Classificado para a final!"
    else:
        mensagem = "Continue treinando para o próximo campeonato!"
    print("\n========== RESULTADO ==========")
    print(f"Resultado: {mensagem}")


if __name__ == "__main__":
    main()
