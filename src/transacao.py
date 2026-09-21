from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conta import Conta


class Transacao(ABC):
    """<<interface>> Transacao"""

    @abstractmethod
    def registrar(self, conta: Conta) -> None:
        """Executa a transação na conta e registra no histórico."""
        ...
