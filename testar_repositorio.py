from dominio.livro import Livro
from dados.repositorio_livro import RepositorioLivro

# Correção: removido o 's' extra de "respositorio"
repositorio = RepositorioLivro()

print("--- GUARDANDO LIVRO NOVO ---")
novo = Livro("Noites Brancas", "Fiodor Dostoiévski", 1848)
repositorio.salvar(novo)
print("Guardado com ID", novo.id)

print("--- BUSCANDO LIVRO ---")
achado = repositorio.buscar_por_id(novo.id)

print("Achado:", achado, "- tipo", type(achado).__name__)

print("--- ATUALIZANDO LIVRO ---")
achado.titulo = " Noites Brancas (edição revisada)"
repositorio.atualizar(achado)
print("Atualizado:", repositorio.buscar_por_id(achado.id))

print("--- EXCLUINDO LIVRO ---")
repositorio.excluir(novo.id)
print("Excluído. Tentando buscar:", repositorio.buscar_por_id(novo.id))

print("--- ACERVO ---")
for livro in repositorio.listar():
    print(livro.id, "-", livro.descricao())




repositorio.fechar()