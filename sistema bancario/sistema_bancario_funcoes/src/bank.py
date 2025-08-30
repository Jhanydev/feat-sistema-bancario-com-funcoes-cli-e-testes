"""
bank.py
Funções puras para operações bancárias: depósito, saque e extrato.
Inclui validações e retorno explícito de estado.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Tuple


@dataclass
class Movimento:
    tipo: str  # "DEPÓSITO" ou "SAQUE"
    valor: float
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class Conta:
    saldo: float = 0.0
    movimentos: List[Movimento] = field(default_factory=list)
    saques_hoje: int = 0  # contador de saques do dia


def depositar(conta: Conta, valor: float) -> Tuple[Conta, str]:
    """
    Realiza depósito.
    - valor deve ser > 0
    Retorna (conta_atualizada, mensagem).
    """
    if valor <= 0:
        return conta, "Valor de depósito inválido. Informe um valor positivo."
    conta.saldo += valor
    conta.movimentos.append(Movimento(tipo="DEPÓSITO", valor=valor))
    return conta, f"Depósito de R$ {valor:,.2f} realizado com sucesso."


def sacar(
    conta: Conta,
    valor: float,
    limite_por_saque: float = 500.0,
    max_saques_dia: int = 3
) -> Tuple[Conta, str]:
    """
    Realiza saque com validações:
    - valor > 0
    - saldo suficiente
    - valor <= limite_por_saque
    - não exceder max_saques_dia
    Retorna (conta_atualizada, mensagem).
    """
    if valor <= 0:
        return conta, "Valor de saque inválido. Informe um valor positivo."
    if valor > conta.saldo:
        return conta, "Saldo insuficiente para saque."
    if valor > limite_por_saque:
        return conta, f"Saque acima do limite permitido (R$ {limite_por_saque:,.2f})."
    if conta.saques_hoje >= max_saques_dia:
        return conta, "Limite diário de saques atingido."
    conta.saldo -= valor
    conta.saques_hoje += 1
    conta.movimentos.append(Movimento(tipo="SAQUE", valor=valor))
    return conta, f"Saque de R$ {valor:,.2f} realizado com sucesso."


def extrato(conta: Conta) -> str:
    """
    Retorna uma string formatada com o histórico e saldo atual.
    """
    linhas = ["=" * 40, "EXTRATO", "-" * 40]
    if not conta.movimentos:
        linhas.append("Nenhuma movimentação realizada.")
    else:
        for m in conta.movimentos:
            carimbo = m.timestamp.strftime("%d/%m/%Y %H:%M:%S")
            linhas.append(f"{carimbo} | {m.tipo:<9} | R$ {m.valor:,.2f}")
    linhas += ["-" * 40, f"SALDO ATUAL: R$ {conta.saldo:,.2f}", "=" * 40]
    return "\n".join(linhas)


def resetar_limites_diarios(conta: Conta) -> Conta:
    """
    Exemplo simples: zera o contador de saques do dia.
    (Em produção, você controlaria a data do último reset.)
    """
    conta.saques_hoje = 0
    return conta
