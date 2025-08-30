"""
cli.py
Interface de linha de comando para o sistema bancário com funções.
"""
from bank import Conta, depositar, sacar, extrato, resetar_limites_diarios

MENU = """
================== MENU ==================
[d] Depositar
[s] Sacar
[e] Extrato
[r] Reset diário de saques
[q] Sair
=========================================
=> """

# Limites (ajuste conforme a regra do desafio)
MAX_SAQUES = 3
LIMITE_SAQUE = 500.0


def main():
    conta = Conta()

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Valor do depósito: R$ ").replace(",", "."))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue
            conta, msg = depositar(conta, valor)
            print(msg)

        elif opcao == "s":
            try:
                valor = float(input("Valor do saque: R$ ").replace(",", "."))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue
            conta, msg = sacar(conta, valor, limite_por_saque=LIMITE_SAQUE, max_saques_dia=MAX_SAQUES)
            print(msg)

        elif opcao == "e":
            print(extrato(conta))

        elif opcao == "r":
            conta = resetar_limites_diarios(conta)
            print("Limites diários de saque foram resetados.")

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
