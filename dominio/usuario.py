class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError ("Nome é obrigatório!")
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        # Parêntese extra removido no final
        return f"{self.nome} ({self.matricula})"