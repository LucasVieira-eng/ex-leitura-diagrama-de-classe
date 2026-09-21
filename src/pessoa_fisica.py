from __future__ import annotations

from datetime import date

from cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: date, cpf: str, endereco: str):
        super().__init__(endereco)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento
