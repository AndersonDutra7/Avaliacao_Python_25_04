from livro import Livro

class Biblioteca:

    lista_de_livros = []

    def __init__(self, nome):
        self.nome = nome
        lista_de_livros = []

    def adicionar_livros(self, livro):
        self.lista_de_livros.append(livro)

    def remover_livros(self, livro):
        if livro in self.lista_de_livros:
            self.lista_de_livros.remove(livro)

