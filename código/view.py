import sqlite3 as lite
import pandas as pd

# conexão
con = lite.connect("dados.db")

# Inserir categoria
def inserir_categoria(c):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, c)

# Inserir receita
def inserir_receita(r):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, add_date, valor) VALUES (?,?,?)"
        cur.execute(query, r)

# Inserir gasto
def inserir_gasto(g):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_date, valor) VALUES (?,?,?)"
        cur.execute(query, g)

# deletando receitas
def deletar_receita(r):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, r)

# deletando gastos
def deletar_gasto(g):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, g)

# vendo categorias
def ver_categoria():
    list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        row = cur.fetchall()

        for r in row:
            list.append(r)

    return list

# vendo receitas
def ver_receitas():
    list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        row = cur.fetchall()

        for r in row:
            list.append(r)

    return list

# vendo gastos
def ver_gastos():
    list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        row = cur.fetchall()

        for r in row:
            list.append(r)

    return list

# função para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)
    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

# função para dados do grafico bar
def bar_valores():
    # receitas totais
    receitas = ver_receitas()
    receitas_list = []

    for i in receitas:
        receitas_list.append(i[3])

    receita_total = sum(receitas_list)

    # despesas totais
    despesas = ver_gastos()
    despesas_list = []

    for i in despesas:
        despesas_list.append(i[3])

    despesas_total = sum(despesas_list)

    # saldo total
    saldo_total = receita_total - despesas_total

    return [receita_total, despesas_total, saldo_total]

# função grafico pizza
def valores_graficoPizza():
    gastos = ver_gastos()
    tabela_list = []
    
    for i in gastos:
        tabela_list.append(i)

    dataframe = pd.DataFrame(tabela_list, columns=['id', 'Categoria', 'Data', 'valor'])
    dataframe = dataframe.groupby('Categoria')['valor'].sum()

    list_qtds = dataframe.values.tolist()
    list_categorias = []

    for i in dataframe.index:
        list_categorias.append(i)

    return ([list_categorias, list_qtds])

# função porcentagem
def valores_porcent():
    # receitas totais
    receitas = ver_receitas()
    receitas_list = []

    for i in receitas:
        receitas_list.append(i[3])

    receita_total = sum(receitas_list)

    # despesas totais
    despesas = ver_gastos()
    despesas_list = []

    for i in despesas:
        despesas_list.append(i[3])

    despesas_total = sum(despesas_list)

    # porcentagem total
    total = ((receita_total - despesas_total)/ receita_total) * 100

    return total

'''print(ver_categoria())
print(ver_gastos())
print(ver_receitas())'''