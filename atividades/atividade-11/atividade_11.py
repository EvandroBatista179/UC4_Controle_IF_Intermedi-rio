# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 11 - IZABELA NO SHOW DE DJAVAN
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
    print("ATIVIDADE 11 — Izabela no Show de Djavan")
    curtidas = ler_inteiro("Quantidade de curtidas", 0)
    comentarios = ler_inteiro("Quantidade de comentários", 0)
    pontos = ler_inteiro("Pontos iniciais", 0)
    if curtidas >= 100 and comentarios >= 30:
        bonus = 50
        final = pontos + bonus
    else:
        bonus = 0
        final = pontos
    print("\n========== RESULTADO ==========")
    print(f"Bônus: {bonus}")
    print(f"Pontuação final: {final}")


if __name__ == "__main__":
    main()
