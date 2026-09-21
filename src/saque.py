from __future__ import annotations

from typing import TYPE_CHECKING

from transacao import Transacao

if TYPE_CHECKING:
    from conta import Conta


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor: float = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta) -> None:
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
