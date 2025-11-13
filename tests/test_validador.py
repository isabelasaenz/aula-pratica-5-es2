import pytest
from validador import ValidadorSenha

def test_senha_valida():
    v = ValidadorSenha("Senha123!")
    valido, msg = v.validar()
    assert valido is True
    assert msg == "Senha válida"

def test_senha_curta():
    v = ValidadorSenha("A1!")
    valido, msg = v.validar()
    assert not valido
    assert "8 caracteres" in msg

def test_sem_maiuscula():
    v = ValidadorSenha("senha123!")
    valido, msg = v.validar()
    assert not valido
    assert "maiúscula" in msg

def test_sem_minuscula():
    v = ValidadorSenha("SENHA123!")
    valido, msg = v.validar()
    assert not valido
    assert "minúscula" in msg

def test_sem_numero():
    v = ValidadorSenha("Senha!!!")
    valido, msg = v.validar()
    assert not valido
    assert "número" in msg

def test_sem_caractere_especial():
    v = ValidadorSenha("Senha123")
    valido, msg = v.validar()
    assert not valido
    assert "caractere especial" in msg
