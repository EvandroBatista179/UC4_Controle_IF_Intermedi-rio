# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 04 - A MARATONA DE SÉRIES
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
    print("ATIVIDADE 04 — A Maratona de Séries")
    caua = ler_inteiro("Cauã disponível? 1=sim, 0=não", 0, 1)
    miguel = ler_inteiro("Miguel disponível? 1=sim, 0=não", 0, 1)
    joao = ler_inteiro("João Victor disponível? 1=sim, 0=não", 0, 1)
    jonatha = ler_inteiro("Jonatha disponível? 1=sim, 0=não", 0, 1)
    if caua == 1 and miguel == 1 and joao == 1 and jonatha == 1:
        mensagem = "Maratona confirmada! Preparem a pipoca!"
    else:
        mensagem = "Maratona não confirmada: há participantes indisponíveis."
    print("\n========== RESULTADO ==========")
    print(f"Resultado: {mensagem}")


if __name__ == "__main__":
    main()
