from __future__ import annotations

from typing import TYPE_CHECKING

from historico import Historico

if TYPE_CHECKING:
    from cliente import Cliente


class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo: float = 0.0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: Cliente = cliente
        self._historico: Historico = Historico()  # composição: nasce e morre com a Conta

    # + saldo(): float  (em Python, uma property é o jeito idiomático)
    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    # + nova_conta(cliente, numero): Conta  (método de classe / factory)
    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> Conta:
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Operação falhou: valor inválido.")
            return False
        if valor > self._saldo:
            print("Operação falhou: saldo insuficiente.")
            return False

        self._saldo -= valor
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Operação falhou: valor inválido.")
            return False

        self._saldo += valor
        return True
