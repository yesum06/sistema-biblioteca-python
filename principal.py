from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

acervo = []
emprestimos = []
usuario = Usuario("Aluno", "0000")

while True:
    print("\n=== BIBLIOTECA\n ===")
    print("1 - Cadastrar livro")
    print("2 - Listar acervo")
    print("3 - Emprestar")
    print("0 - Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        
        # O try agora protege tanto a digitação de letras no ano quanto as regras da classe
        try:
            ano = int(input("Ano: "))
            acervo.append(Livro(titulo, autor, ano))
            print("Livro cadastrado!")
        except ValueError as erro:
            print("Não deu: ", erro)
                    
    elif opcao == "2":
        if not acervo:
            print("Acervo vazio.")
        for livro in acervo:
            print("-", livro)
            
    elif opcao == "3":
        procurado = input("Título: ")
        escolhido = None

        for livro in acervo:
            if livro.titulo.lower() == procurado.lower():
                escolhido = livro

        # Agora este bloco está corretamente dentro da opção 3
        if escolhido is None:
            print("Não está no acervo.")
        else:
            emprestimos.append(Emprestimo(escolhido, usuario, "30/08/2026"))  
            print("Emprestado: ", emprestimos[-1])  

    elif opcao == "0":
        print("Até logo!")
        break # Encerra o laço while e finaliza o programa
   
    else:
        print("Opção Inválida")
    
