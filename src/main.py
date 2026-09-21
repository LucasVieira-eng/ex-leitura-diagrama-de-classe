from datetime import date

from conta_corrente import ContaCorrente
from deposito import Deposito
from pessoa_fisica import PessoaFisica
from saque import Saque


def main() -> None:
    cliente = PessoaFisica(
        nome="Maria Silva",
        data_nascimento=date(2000, 1, 15),
        cpf="123.456.789-00",
        endereco="Rua A, 100 - São Paulo/SP",
    )

    conta = ContaCorrente.nova_conta(cliente, numero=1)
    cliente.adicionar_conta(conta)

    cliente.realizar_transacao(conta, Deposito(1000))
    cliente.realizar_transacao(conta, Saque(200))
    cliente.realizar_transacao(conta, Saque(600))  # falha: acima do limite por saque

    print(f"Saldo: R$ {conta.saldo:.2f}")
    for t in conta.historico.transacoes:
        print(f"- {type(t).__name__}: R$ {t.valor:.2f}")


if __name__ == "__main__":
    main()
