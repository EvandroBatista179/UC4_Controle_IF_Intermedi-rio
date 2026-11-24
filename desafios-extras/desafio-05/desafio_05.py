# UC4 - DESENVOLVER ALGORITMOS
# DESAFIO 05 - O FESTIVAL DE TALENTOS DA TURMA
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
    print("DESAFIO 05 — O Festival de Talentos da Turma")
    participantes = ler_inteiro("Participantes inscritos", 0)
    orcamento = ler_decimal("Orçamento disponível (R$)", 0)
    if participantes >= 20 and orcamento >= 500:
        bonus = 200.0
        final = orcamento + bonus
        mensagem = "Festival aprovado!"
    else:
        bonus = 0.0
        final = orcamento
        mensagem = "Festival não aprovado"
    print("\n========== RESULTADO ==========")
    print(f"Resultado: {mensagem}")
    print(f"Patrocínio extra (R$): {bonus:.2f}")
    print(f"Orçamento final (R$): {final:.2f}")


if __name__ == "__main__":
    main()
