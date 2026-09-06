import sqlite3

# banco é um ARQUIVO. se ele não existir, ele será criado automaticamente. Se ele já existir, ele será aberto.
conexao = sqlite3.connect('biblioteca.db')

# o cursor é o objeto que permite executar comandos SQL no banco de dados
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livro (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor  TEXT,
        ano    INTEGER
    )    
""")

print("Tabela criada com sucesso!")

# cada ? é um buraco que o python preenche com um valor da tupla, na ordem
# Para inserir múltiplos registros, usamos executemany e passamos uma LISTA de tuplas
cursor.executemany(
    "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
    [ 
        ("A Vegetariana", "Han Kang", 2007),
        ("Carmilla", "Sheridan Le Fu", 1872),
        ("A Redoma de Vidro", "Sylvia Plath",1963),
        ("A Hora da Estrela", "Clarisse Lispector", 1977),
        ("A Metamorfose","Franz Kafka",1915)
    ]        
         
)

print("Inserido")

conexao.commit()  # confirma as alterações no banco de dados

cursor.execute("SELECT id, titulo, autor, ano FROM livro")

#fetchall() retorna uma lista de tuplas, cada tupla é uma linha do resultado da consulta
for codigo, titulo, autor, ano in cursor.fetchall():
    print(f"{codigo} - {titulo} - {autor} ({ano})")

conexao.close()