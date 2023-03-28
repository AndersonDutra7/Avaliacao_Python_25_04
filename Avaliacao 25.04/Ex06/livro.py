# 6- Crie uma classe Livro que tenha os atributos título, autor e ano.
# Crie um método na classe para imprimir as informações do livro.
# Crie uma classe Biblioteca que tenha uma lista de livros e métodos para adicionar e remover livros da lista.
# Crie um objeto da classe Biblioteca, adicione alguns livros à lista, e imprima as informações dos livros da lista.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def informacoes_do_livro(self):
        print(f'Título: {self.titulo} - Autor: {self.autor} - Ano: {self.ano}.')