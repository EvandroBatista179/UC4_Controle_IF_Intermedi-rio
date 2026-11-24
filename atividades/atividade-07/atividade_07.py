# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 07 - A MÚSICA DE AMOR DE WANDERCYRA
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
    print("ATIVIDADE 07 — A Música de Amor de Wandercyra")
    plays = ler_inteiro("Número de reproduções", 0)
    curtidas = ler_inteiro("Quantidade de curtidas", 0)
    arrecadado = ler_decimal("Valor já arrecadado (R$)", 0)
    if plays > 1000 or curtidas > 200:
        bonus = 150.0
        final = arrecadado + bonus
    else:
        bonus = 0.0
        final = arrecadado
    print("\n========== RESULTADO ==========")
    print(f"Bônus (R$): {bonus:.2f}")
    print(f"Arrecadação final (R$): {final:.2f}")


if __name__ == "__main__":
    main()
