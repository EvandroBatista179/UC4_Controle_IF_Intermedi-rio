# UC4 - DESENVOLVER ALGORITMOS
# ATIVIDADE 14 - A PROMESSA DE ESFIHA DA PROF. RUTH
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
    print("ATIVIDADE 14 — A Promessa de Esfiha da Prof. Ruth")
    alunos = ler_inteiro("Total de alunos", 0)
    presentes = ler_inteiro("Alunos presentes", 0)
    media = ler_decimal("Média da turma (0 a 10)", 0, 10)
    if presentes == alunos and media >= 8:
        total = alunos * 5.0
        mensagem = "Compra autorizada"
    else:
        total = 0.0
        mensagem = "Compra não autorizada"
    print("\n========== RESULTADO ==========")
    print(f"Situação: {mensagem}")
    print(f"Custo total (R$): {total:.2f}")


if __name__ == "__main__":
    main()
