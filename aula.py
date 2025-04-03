class ContaCorrente:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Valor de depósito inválido. O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor de saque inválido. O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Erro: Valor de transferência inválido. O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente para realizar a transferência.")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso para a conta {conta_destino.numero_conta}.")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular} (Conta {self.numero_conta}): R${self.saldo:.2f}")


def obter_valor(valor_tipo):
    while True:
        try:
            valor = float(input(f"Digite o valor para {valor_tipo}: R$"))
            if valor > 0:
                return valor
            else:
                print("Erro: O valor deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")


def main():
    
    conta1 = ContaCorrente("João", 12345)
    conta2 = ContaCorrente("Maria", 67890)
    
    print("Bem-vindo ao Sistema Bancário!\n")

    
    while True:
        print("\nSelecione uma operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Transferir")
        print("4 - Consultar Saldo")
        print("5 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            valor = obter_valor("depósito")
            conta1.depositar(valor)
            conta1.consultar_saldo()
        elif opcao == "2":
            valor = obter_valor("saque")
            conta1.sacar(valor)
            conta1.consultar_saldo()
        elif opcao == "3":
            valor = obter_valor("transferência")
            conta1.transferir(valor, conta2)
            conta1.consultar_saldo()
            conta2.consultar_saldo()
        elif opcao == "4":
            conta1.consultar_saldo()
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Erro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
