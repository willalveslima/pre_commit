import pytest
from codigo.main import soma, Pessoa

def test_cumprimentar():
    pessoa = Pessoa("João", 30)
    assert pessoa.cumprimentar() == "Olá, meu nome é João e eu tenho 30 anos."

def test_soma():
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0
    assert soma(-1, -1) == -2

def test_soma_floats():
    assert soma(1.5, 2.5) == 4.0
    assert soma(-1.5, 1.5) == 0.0
    assert soma(-1.5, -1.5) == -3.0

def test_soma_large_numbers():
    assert soma(1000000, 2000000) == 3000000
    assert soma(-1000000, 1000000) == 0
    assert soma(-1000000, -1000000) == -2000000

def test_cumprimentar_different_names():
    pessoa = Pessoa("Maria", 25)
    assert pessoa.cumprimentar() == "Olá, meu nome é Maria e eu tenho 25 anos."
    pessoa = Pessoa("Carlos", 40)
    assert pessoa.cumprimentar() == "Olá, meu nome é Carlos e eu tenho 40 anos."

def test_cumprimentar_edge_cases():
    pessoa = Pessoa("", 0)
    assert pessoa.cumprimentar() == "Olá, meu nome é  e eu tenho 0 anos."
    pessoa = Pessoa("Ana", -1)
    assert pessoa.cumprimentar() == "Olá, meu nome é Ana e eu tenho -1 anos."