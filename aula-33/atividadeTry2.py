produtos = [
        {
            'id': 1,
            'produto': 'Ovo',
            'valor': 30
        },
        {
            'id': 2,
            'produto': 'Whey',
            'valor': 100
        },
        {
            'id': 3,
            'produto': 'Leite',
            'valor': 3.50
        }
]

def buscar(lista, id_produto):
    try:
        for item in lista:
            if(item.get('id') == id_produto):
                print(f"O produto selecionado {item}")
                return item
        
        raise ValueError("Produto não encontrado") #Forçar a dar erro caso n encontre o id_produto

    except ValueError as e:
        print(e)

res = buscar(produtos, 2)
