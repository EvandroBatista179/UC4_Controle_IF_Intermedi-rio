# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 09 - A PALESTRA SOBRE CASAMENTO
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
    print("ATIVIDADE 09 — A Palestra sobre Casamento")
    inscritos = ler_inteiro("Quantidade de inscritos", 0)
    cadeiras = ler_inteiro("Cadeiras disponíveis", 0)
    if inscritos > 80 and cadeiras < inscritos:
        adicionadas = 30
        final = cadeiras + adicionadas
    else:
        adicionadas = 0
        final = cadeiras
    print("\n========== RESULTADO ==========")
    print(f"Cadeiras acrescentadas: {adicionadas}")
    print(f"Cadeiras finais: {final}")


if __name__ == "__main__":
    main()
