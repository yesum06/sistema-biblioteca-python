# importando a biblioteca para a criação de interfaces/janelas gráficas
import tkinter as tk

# o dominio NÃO MUDA. a janela só importa o que já existe
from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

acervo = [
        Livro("A Vegetariana", "Han Kang", 2007),
        Livro("Carmilla", "Sheridan Le Fu", 1872),
        Livro("A Redoma de Vidro", "Sylvia Plath",1963),
        Livro("A Hora da Estrela", "Clarisse Lispector", 1977),
        Livro("A Metamorfose","Franz Kafka",1915)
]

emprestimos = []
usuario = Usuario("Aluno", "0000")
    
janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("460x560")  #largura x altura, em pixels

tk.Label(janela, text="Acervo", font=("CS Flexion", 14)).pack(pady=6)

lista = tk.Listbox(janela, width=52, height=6)
for livro in acervo:
    lista.insert(tk.END,str(livro))
lista.pack(padx=10) 

campo = tk.Entry(janela, width=34)
campo.pack(pady=8)

#criando agora,mas só aparece na tela lá embaixo,depois dos botões
resultado = tk.Label(janela, text="", fg="blue")

def emprestar():
    procurado = campo.get()

    escolhido = None
    for item in acervo:
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
    for livro in acervo:
       lista.insert(tk.END, str(livro))


def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()

    try:
        livro = Livro(titulo, autor, int(ano))
        acervo.append(livro)
        atualizar_lista()
        campo_titulo.delete(0, tk.END)
        campo_autor.delete(0, tk.END)
        campo_ano.delete(0, tk.END)
        resultado.config(text="Cadastrado: " + str(livro), fg="blue")
    except ValueError as erro:
        resultado.config(text=str(erro),fg="red")

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=6)  



   


janela.mainloop()