"""Módulo principal do projeto."""


class Pessoa:
    """Classe que representa uma pessoa."""

    def __init__(self, nome: str, idade: int):
        """
        __init__ Método construtor da classe Pessoa.

        Args:
            nome (str): nome da pessoa
            idade (int): idade da pessoa
        """
        self.nome = nome
        self.idade = idade

    def cumprimentar(self) -> str:
        """
        Cumprimentar comprimenta a pessoa.

        Returns:
            str: Uma mensagem de cumprimento.
        """
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


def soma(a: int, b: int) -> int:
    """
    Soma soma dois números.

    Args:
        a (int): parcela 1
        b (int): parcela 2

    Returns:
        int: soma dos dois números
    """
    return a + b


# Exemplo de uso
pessoa = Pessoa("João", 30)
print(pessoa.cumprimentar())
