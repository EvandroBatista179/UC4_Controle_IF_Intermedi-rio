# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 05 - MIKAELLY E O SHOW DO BTS
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
    print("ATIVIDADE 05 — Mikaelly e o Show do BTS")
    guardado = ler_decimal("Dinheiro guardado (R$)", 0)
    custo = 750.0 + 300.0
    if guardado >= custo:
        bonus = 100.0
        final = guardado + bonus
    else:
        bonus = 0.0
        final = guardado
    print("\n========== RESULTADO ==========")
    print(f"Custo ingresso + passagem (R$): {custo:.2f}")
    print(f"Bônus da família (R$): {bonus:.2f}")
    print(f"Dinheiro após bônus (R$): {final:.2f}")


if __name__ == "__main__":
    main()
