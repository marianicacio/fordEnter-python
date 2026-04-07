produtos = [
    {
        'id': 0,
        'name': 'Mouse Pad',
        'price': 20.50
    },
    {
        'id': 1,
        'name': 'Teclado',
        'price': 120.50
    },
    {
        'id': 2,
        'name': 'Fone Gaymer',
        'price': 200.30
    }
]

print(f"Preço: {produtos[1]}")

del produtos[1] #del e usado para excluir um item de um dicionario

print(produtos)