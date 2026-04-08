def pessoas(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f"{nome} tem atualmente {idade} anos de idades")

pessoas(Maria=18, Murillo=19)