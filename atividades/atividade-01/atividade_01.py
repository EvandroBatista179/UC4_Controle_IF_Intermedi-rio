# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 01 - A LOJINHA DE VARIEDADES DE LIZANDRA
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
    print("ATIVIDADE 01 — A Lojinha de Variedades de Lizandra")
    compra = ler_decimal("Valor total da compra (R$)", 0)
    if compra > 150:
        desconto = 30.0
        final = compra - desconto
    else:
        desconto = 0.0
        final = compra
    print("\n========== RESULTADO ==========")
    print(f"Desconto (R$): {desconto:.2f}")
    print(f"Valor a pagar (R$): {final:.2f}")


if __name__ == "__main__":
    main()
