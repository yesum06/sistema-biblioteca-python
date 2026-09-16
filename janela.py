# importando a biblioteca para a criação de interfaces/janelas gráficas
import tkinter as tk

# o dominio NÃO MUDA. a janela só importa o que já existe
from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

# a janela passa a conhecer o repositório - e continua sem conhecer o SQLite
from dados.repositorio_livro import RepositorioLivro

repositorio = RepositorioLivro()

# o que a ListBox está mostrando agora, na mesma ordem da tela
livros_na_tela = []

emprestimos = []
usuario = Usuario("Aluno", "0000")
    
janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("460x560")  #largura x altura, em pixels

tk.Label(janela, text="Acervo", font=("CS Flexion", 14)).pack(pady=6)

lista = tk.Listbox(janela, width=52, height=6)

lista.pack(padx=10) 

campo = tk.Entry(janela, width=34)
campo.pack(pady=8)

#criando agora,mas só aparece na tela lá embaixo,depois dos botões
resultado = tk.Label(janela, text="", fg="blue")

def emprestar():
    procurado = campo.get()

    escolhido = None
    for item in repositorio.listar():
          if item.titulo.lower() == procurado.lower():
               escolhido = item

    if escolhido is None:
        resultado.config(text= "Não está no acervo!", fg="red")
        return
    
    emprestimo = Emprestimo(escolhido, usuario, "27/08/2026")  
    emprestimos.append(emprestimo)
    resultado.config(text="Emprestado: " + str(emprestimo), fg="blue")

def devolver():
    if not emprestimos:
          resultado.config(text="Não há empréstimo!", fg="red")
          return

    emprestimo = emprestimos[-1]
    
    try:
         emprestimo.devolver()
         resultado.config(text="Devolvido: " + str(emprestimo), fg="blue")
    except ValueError as erro:
         # a classe recusou. quem MOSTRA e a janela
         resultado.config(text=str(erro), fg="red")     

tk.Button(janela, text="Emprestar", command=emprestar).pack()
tk.Button(janela, text="Devolver", command=devolver).pack(pady=4)

resultado.pack(pady=6)

titulo_secao = tk.Label(janela, text="Cadastrar livro", font=("Arial", 12))
titulo_secao.pack(pady=(10, 4))

formulario = tk.Frame(janela)
formulario.pack()

tk.Label(formulario, text="Titulo:").grid(row=0, column=0, sticky="e")
campo_titulo = tk.Entry(formulario, width=28)
campo_titulo.grid(row=0, column=1, pady=2)

tk.Label(formulario, text="Autor:").grid(row=1, column=0, sticky="e")
campo_autor = tk.Entry(formulario, width=28)
campo_autor.grid(row=1, column=1, pady=2)

tk.Label(formulario, text="Ano:").grid(row=2, column=0, sticky="e")
campo_ano = tk.Entry(formulario, width=28)
campo_ano.grid(row=2, column=1, pady=2)


def atualizar_lista():
    lista.delete(0, tk.END)

# a tela não guarda nada: ela mostra o que o repositório devolveu agora
    livros_na_tela.clear()

# o for que estava aqui percorria acervo. agora ele percorre o banco
    for livro in repositorio.listar():
         livros_na_tela.append(livro)
         lista.insert(tk.END, str(livro))

def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()

    try:
        livro = Livro(titulo, autor, int(ano))
        # antes era acervo.append(livro) - e sumia ao fechar a janela
        repositorio.salvar(livro)
        atualizar_lista()
        campo_titulo.delete(0, tk.END)
        campo_autor.delete(0, tk.END)
        campo_ano.delete(0, tk.END)
        resultado.config(text="Cadastrado: " + str(livro), fg="blue")
    except ValueError as erro:
        resultado.config(text=str(erro),fg="red")

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=6)

def excluir ():
     livro= livro_selecionado()

     if livro is None:
          return

     # quem some do banco e o id, nao a linha da tela
     repositorio.excluir(livro.id)
     atualizar_lista()
     resultado.config(text="Excluído: " + livro.titulo, fg="blue")

botoes = tk.Frame(janela)
botoes.pack()

tk.Button(botoes, text="Excluir", command=excluir).pack(side="left", padx=4)


def alterar():
     livro = livro_selecionado()

     if livro is None:
          return
     try:
          # a regra continua na classe: ano inválido não entra no banco
          # porque o setter do dominio recusa antes
          livro.titulo = campo_titulo.get()
          livro.autor = campo_autor.get()
          livro.ano = int(campo_ano.get())

          repositorio.atualizar(livro)
          atualizar_lista()
          resultado.config(text="Alterado: " + str(livro), fg="blue")
     except ValueError as erro:
         resultado.config(text=str(erro), fg="red")

# a primeira carga da tela: ela nasce vazia e o banco a preenche
atualizar_lista()

def livro_selecionado():
     selecionados = lista.curselection()

     if not selecionados:
          resultado.config(text= "Selecione um livro na lista.", fg="red")
          return None

     # a posição na tela NÃO e o id do banco - ela só serve para achar o objeto
     posicao = selecionados[0]
     return livros_na_tela[posicao]
     
tk.Button(botoes, text="Alterar", command=alterar).pack(side="left", padx=4)

janela.mainloop()

# quando a janela fecha, a conexão fecha junto
repositorio.fechar()