from datetime import date
class Livro:
    def __init__(self, titulo, autor, ano): 
        if not titulo:
            raise ValueError("O título do livro é obrigatório")
        if not autor:
            raise ValueError("O autor do livro é obrigatório")
        
        self.titulo = titulo 
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano  

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > date.today().year:
            raise ValueError(f"Ano inválido: {valor}")
        self._ano = valor

    # Os métodos abaixo voltaram para dentro da classe Livro
    def descricao(self):
        return  f"{self.titulo} - {self.autor} ({self.ano})"
        
    def __str__(self):
        return self.descricao()
    

    def idade(self):
        return date.today().year - self.ano

    def e_classico(self):
        return self.idade() > 100

        