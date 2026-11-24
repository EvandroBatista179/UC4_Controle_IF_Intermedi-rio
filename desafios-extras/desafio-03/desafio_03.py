# UC4 - DESENVOLVER ALGORITMOS
# DESAFIO 03 - MIKAELLY E O ORÇAMENTO DO SHOW DO BTS
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
    print("DESAFIO 03 — Mikaelly e o Orçamento do Show do BTS")
    guardado = ler_decimal("Dinheiro disponível (R$)", 0)
    custo = 900.0 + 600.0 + 400.0
    if guardado >= custo:
        diferenca = guardado - custo
        mensagem = "Mikaelly vai realizar seu sonho!"
        detalhe = "Dinheiro que sobrará"
    else:
        diferenca = custo - guardado
        mensagem = "Ainda falta economizar!"
        detalhe = "Dinheiro que falta"
    print("\n========== RESULTADO ==========")
    print(f"Custo total da viagem (R$): {custo:.2f}")
    print(f"Resultado: {mensagem}")
    print(f"{detalhe}: R$ {diferenca:.2f}")


if __name__ == "__main__":
    main()
