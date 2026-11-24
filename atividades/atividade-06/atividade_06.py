# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 06 - A AULA DE LÓGICA DE ESTEFANY
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
    print("ATIVIDADE 06 — A Aula de Lógica de Estefany")
    nota = ler_decimal("Nota de Marli (0 a 10)", 0, 10)
    exercicios = ler_inteiro("Exercícios entregues", 0)
    if nota >= 7 and exercicios >= 5:
        bonus = 2.0
        final = nota + bonus
    else:
        bonus = 0.0
        final = nota
    print("\n========== RESULTADO ==========")
    print(f"Bônus (pontos): {bonus:.2f}")
    print(f"Nota final: {final:.2f}")


if __name__ == "__main__":
    main()
