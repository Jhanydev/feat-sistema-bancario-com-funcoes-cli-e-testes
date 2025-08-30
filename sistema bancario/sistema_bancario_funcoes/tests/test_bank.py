import builtins
from src.bank import Conta, depositar, sacar, extrato, resetar_limites_diarios

def test_deposito_valido():
    c = Conta()
    c, msg = depositar(c, 100)
    assert c.saldo == 100
    assert "sucesso" in msg.lower()

def test_deposito_invalido():
    c = Conta()
    c, msg = depositar(c, -10)
    assert c.saldo == 0
    assert "inválido" in msg.lower()

def test_saque_valido():
    c = Conta(saldo=600)
    c, msg = sacar(c, 100, limite_por_saque=500, max_saques_dia=3)
    assert c.saldo == 500
    assert c.saques_hoje == 1

def test_saque_acima_limite():
    c = Conta(saldo=1000)
    c, msg = sacar(c, 600, limite_por_saque=500, max_saques_dia=3)
    assert c.saldo == 1000
    assert "limite permitido" in msg.lower()

def test_saque_sem_saldo():
    c = Conta(saldo=50)
    c, msg = sacar(c, 100, limite_por_saque=500, max_saques_dia=3)
    assert c.saldo == 50
    assert "saldo insuficiente" in msg.lower()

def test_limite_diario_saques():
    c = Conta(saldo=1000, saques_hoje=3)
    c, msg = sacar(c, 100, limite_por_saque=500, max_saques_dia=3)
    assert c.saldo == 1000
    assert "limite diário" in msg.lower()

def test_extrato_formato():
    c = Conta()
    c, _ = depositar(c, 200)
    c, _ = sacar(c, 50)
    txt = extrato(c)
    assert "EXTRATO" in txt
    assert "DEPÓSITO" in txt
    assert "SAQUE" in txt

def test_resetar_limites():
    c = Conta(saques_hoje=2)
    c = resetar_limites_diarios(c)
    assert c.saques_hoje == 0
