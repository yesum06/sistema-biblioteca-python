class Emprestimo:
    def __init__ (self, livro, usuario, data):
        self.livro = livro
        self.usuario = usuario
        self.data = data
        self.devolvido = False

    def devolver (self):
        if self.devolvido:
            raise ValueError("Este empréstimo já foi devolvido!")
        self.devolvido = True

    def __str__ (self):
        estado = "devolvido" if self.devolvido else "em aberto"
        # Parêntese extra removido no final
        return f"{self.livro.titulo} -> {self.usuario.nome} ({estado})"    


#if __name__ == "__main__":
    #livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
    
    #ana = Usuario("Ana Souza", "2026001")
    #emp = Emprestimo(livro, ana, "20/08/2026")

    #print(emp)
    #print(emp.livro.autor)
    #print(emp.usuario.matricula)

    #emp.devolver()
    #print(emp)
    
    # Esta linha deve estourar um ValueError de propósito
    #emp.devolver()