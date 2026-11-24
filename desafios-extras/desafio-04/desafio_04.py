# UC4 - DESENVOLVER ALGORITMOS
# DESAFIO 04 - O GRANDE PEDIDO DE ESFIHA
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
    print("DESAFIO 04 — O Grande Pedido de Esfiha")
    quantidade = ler_inteiro("Quantidade de esfihas", 0)
    if quantidade >= 30:
        preco_unitario = 4.0
    else:
        preco_unitario = 5.0
    total = quantidade * preco_unitario
    print("\n========== RESULTADO ==========")
    print(f"Preço unitário (R$): {preco_unitario:.2f}")
    print(f"Custo total (R$): {total:.2f}")


if __name__ == "__main__":
    main()
