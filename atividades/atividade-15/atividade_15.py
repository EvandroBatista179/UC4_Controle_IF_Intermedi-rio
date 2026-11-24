# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 15 - O COMPUTADOR MISTERIOSO DO LABORATÓRIO
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
    print("ATIVIDADE 15 — O Computador Misterioso do Laboratório")
    ocupado = ler_inteiro("Estado do computador (1=ocupado; 0=livre)", 0, 1)
    if not bool(ocupado):
        mensagem = "Computador disponível! Atualização autorizada."
    else:
        mensagem = "Computador ocupado. Atualização não autorizada."
    print("\n========== RESULTADO ==========")
    print(f"Resultado: {mensagem}")


if __name__ == "__main__":
    main()
