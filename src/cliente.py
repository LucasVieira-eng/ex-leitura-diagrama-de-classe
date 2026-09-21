from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conta import Conta
    from transacao import Transacao


class Cliente:
    def __init__(self, endereco: str):
        self._endereco: str = endereco
        self._contas: list[Conta] = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list[Conta]:
        return self._contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta) -> None:
        self._contas.append(conta)
