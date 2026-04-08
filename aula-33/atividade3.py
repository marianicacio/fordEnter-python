def lista_compras(**produtosValor):
    lista = [
        {
            'produto': 'Ovo',
            'valor': 30
        },
        {
            'produto': 'Whey',
            'valor': 100
        },
        {
            'produto': 'Leite',
            'valor': 3.50
        }
    ]

    total = sum(item['valor'] for item in lista)
    
    print(f"Preço do primeiro {lista[0]}")
    print(f"Preço do segundo {lista[1]}")
    print(f"Preço do terceiro {lista[2]}")
    print(f"Valor total: {total}")
    

lista_compras()