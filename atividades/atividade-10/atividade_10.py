# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 10 - AS COMPRAS DE KAUANE E KAUANY
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
    print("ATIVIDADE 10 — As Compras de Kauane e Kauany")
    livros = ler_inteiro("Quantidade de livros", 0)
    jogos = ler_inteiro("Quantidade de jogos", 0)
    compra = ler_decimal("Valor da compra (R$)", 0)
    if livros >= 2 or jogos >= 3:
        desconto = 25.0
        final = compra - desconto
    else:
        desconto = 0.0
        final = compra
    print("\n========== RESULTADO ==========")
    print(f"Desconto (R$): {desconto:.2f}")
    print(f"Valor final (R$): {final:.2f}")


if __name__ == "__main__":
    main()
