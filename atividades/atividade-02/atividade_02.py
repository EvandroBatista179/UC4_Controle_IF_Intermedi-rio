# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 02 - ANNA BEATRIZ E GIULIANY NO MCDONALD'S
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
    print("ATIVIDADE 02 — Anna Beatriz e Giuliany no McDonald's")
    anna = ler_decimal("Gasto de Anna Beatriz (R$)", 0)
    giuliany = ler_decimal("Gasto de Giuliany (R$)", 0)
    total = anna + giuliany
    if total > 80:
        bonus = 20.0
        final = total + bonus
    else:
        bonus = 0.0
        final = total
    print("\n========== RESULTADO ==========")
    print(f"Total gasto (R$): {total:.2f}")
    print(f"Acréscimo (R$): {bonus:.2f}")
    print(f"Resultado final (R$): {final:.2f}")


if __name__ == "__main__":
    main()
