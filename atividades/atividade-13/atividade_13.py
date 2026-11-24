# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 13 - BRENO E ARTUR EXPLORANDO O SENAC
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
    print("ATIVIDADE 13 — Breno e Artur Explorando o SENAC")
    laboratorios = ler_inteiro("Laboratórios visitados", 0)
    base = laboratorios * 10
    if laboratorios >= 4:
        bonus = 20
        final = base + bonus
    else:
        bonus = 0
        final = base
    print("\n========== RESULTADO ==========")
    print(f"Pontos das visitas: {base}")
    print(f"Bônus: {bonus}")
    print(f"Pontuação final: {final}")


if __name__ == "__main__":
    main()
