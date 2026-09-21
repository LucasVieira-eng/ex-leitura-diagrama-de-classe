from __future__ import annotations

from typing import TYPE_CHECKING

from conta import Conta
from saque import Saque

if TYPE_CHECKING:
    from cliente import Cliente


class ContaCorrente(Conta):
    def __init__(
        self,
        numero: int,
        cliente: Cliente,
        limite: float = 500.0,
        limite_saques: int = 3,
    ):
        super().__init__(numero, cliente)
        self._limite: float = limite              # valor máximo por saque
        self._limite_saques: int = limite_saques  # nº máximo de saques

    def sacar(self, valor: float) -> bool:
        numero_saques = sum(
            1 for t in self.historico.transacoes if isinstance(t, Saque)
        )

        if valor > self._limite:
            print("Operação falhou: valor excede o limite por saque.")
            return False
        if numero_saques >= self._limite_saques:
            print("Operação falhou: limite de saques atingido.")
            return False

        return super().sacar(valor)
