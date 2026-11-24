# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 03 - O PROGRAMA DA NINTENDO CRIADO POR JULIO
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
    print("ATIVIDADE 03 — O Programa da Nintendo Criado por Julio")
    jogos = ler_inteiro("Quantidade de jogos", 0)
    compra = ler_decimal("Total gasto (R$)", 0)
    pontos = ler_inteiro("Pontuação inicial", 0)
    if jogos >= 3 and compra > 500:
        bonus = 200
        final = pontos + bonus
    else:
        bonus = 0
        final = pontos
    print("\n========== RESULTADO ==========")
    print(f"Bônus (pontos): {bonus}")
    print(f"Pontuação final: {final}")


if __name__ == "__main__":
    main()
