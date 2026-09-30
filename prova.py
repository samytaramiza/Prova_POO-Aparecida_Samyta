from __future__ import annotations
from datetime import date

class QuantidadeInvalidaError (Exception): pass
class MedicamentoVencidoError (Exception): pass

class Medicamento:
    def __init__ (self, nome: str, lote: str, validade: date, quantidade: int, valor: float):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

    @property 
    def exibir_quantidade (self):
        return self._quantidade

    @quantidade.setter
    def quantidade (self):
        if valor < 0 :
            raise ValueError ("Quantidade não pode ser negativa!")
            self._valor = valor

    @property 
    def exibir_valor (self):
        return self.valor

        
