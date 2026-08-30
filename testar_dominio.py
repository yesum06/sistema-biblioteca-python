# cada classe agora mora no proprio arquivo, dentro ds pasta dominio
from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

print("--- testando o dominio, sem tela nenhuma ---")

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
print("Livro Criado: ", livro)

# o teste tem que provar que o ERRADO também é barrado
try:
    Livro("Sem ano", "Alguem", 3000)
    print("FALHOU: o ano 3000 passou")
except ValueError as erro:
    print("ok, barrou: ", erro)

ana = Usuario("Ana Souza", "2026001")
emp = Emprestimo(livro, ana, "24/08/2026")
print("Empréstimo: ", emp)

emp.devolver()
print("Depois de devolver: ", emp)

try:
    emp.devolver()
    print("FALHOU: devolveu duas vezes")
except ValueError as erro:
    print("Ok, barrou: ", erro)

acervo = [
    livro,
    Livro("Iracema", "Jose de Alencar",1865),
]   

print("Livros no acervo: ", len(acervo)) #len() conta a qtd de itens na lista
print("O autor do primeiro: ", acervo[0].autor)

# buscar, percorrer e comparar
procurado = "iracema"
escolhido = None
for item in acervo:
    if item.titulo.lower() == procurado.lower():
        escolhido = item
print("Escolhido: ", escolhido)

# [] com for dentro = filtro
emprestimos = [emp, Emprestimo(acervo[1], ana, "24/08/2026")]
#leia: "os emprestimos, um por um, osque NAO foram devolvidos"
em_aberto = [e for e in emprestimos if not e.devolvido]
print("emprstimos:", len(emprestimos), "- em aberto:", len(em_aberto))