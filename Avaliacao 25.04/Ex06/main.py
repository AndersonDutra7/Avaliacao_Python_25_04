from livro import  Livro
from biblioteca import Biblioteca

l1 = Livro('A Mágica de Python' , 'Titione Tio Tone', 2023)
l2 = Livro('Soltando as Frangas', 'Agnaldo Helsinki', 2020)
l3 = Livro("Entre a Ordem e o Caos", "Jordan Peterson", 2021)
biblio1 = Biblioteca('Biblioteca Municipal Exercicio 06')

biblio1.adicionar_livros(l1)
biblio1.adicionar_livros(l2)
biblio1.adicionar_livros(l3)

print(biblio1.nome)
for livro in biblio1.lista_de_livros:
    if livro.informacoes_do_livro() is not None:
        print(livro.informacoes_do_livro())

print("\033[1;32m#" * 70 + "\033[0m\n")

biblio1.remover_livros(l2)
print(biblio1.nome)
for livro in biblio1.lista_de_livros:
    if livro.informacoes_do_livro() is not None:
        print(livro.informacoes_do_livro())