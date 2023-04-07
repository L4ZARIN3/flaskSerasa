import sqlite3

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('databases/srs_telefones.db')

# Crie um cursor para executar consultas
cursor = conn.cursor()

# Substitua 'nome_da_tabela' pelo nome da tabela que você deseja consultar
table_name = 'SRS_HISTORICO_TELEFONES'

# Execute a consulta para obter informações sobre as colunas da tabela
cursor.execute("PRAGMA table_info({})".format(table_name))

# Use o método fetchall() para obter todas as linhas de resultados da consulta
result = cursor.fetchall()

# Extraia o nome de cada coluna da tabela e armazene em uma lista
column_names = [row[1] for row in result]

# Imprima o nome de cada coluna da tabela
for column in column_names:
    print(column)

# Feche o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
