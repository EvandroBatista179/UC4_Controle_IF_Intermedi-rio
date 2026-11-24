# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 12 - FELIPE E AS TRANÇAS DE MILENA
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
    print("ATIVIDADE 12 — Felipe e as Tranças de Milena")
    distancia = ler_decimal("Distância percorrida (km)", 0)
    base = 180.0
    if distancia > 10:
        taxa = 25.0
        final = base + taxa
    else:
        taxa = 0.0
        final = base
    print("\n========== RESULTADO ==========")
    print(f"Valor do serviço (R$): {base:.2f}")
    print(f"Taxa de deslocamento (R$): {taxa:.2f}")
    print(f"Total a pagar (R$): {final:.2f}")


if __name__ == "__main__":
    main()
