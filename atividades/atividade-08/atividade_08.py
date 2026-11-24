# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 08 - A EXTENSÃO DE RAP DO VS CODE
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
    print("ATIVIDADE 08 — A Extensão de Rap do VS Code")
    execucoes = ler_inteiro("Quantidade de execuções", 0)
    musicas = ler_inteiro("Músicas disponíveis inicialmente", 0)
    if execucoes >= 10:
        bonus = 5
        final = musicas + bonus
    else:
        bonus = 0
        final = musicas
    print("\n========== RESULTADO ==========")
    print(f"Novas músicas: {bonus}")
    print(f"Total de músicas: {final}")


if __name__ == "__main__":
    main()
