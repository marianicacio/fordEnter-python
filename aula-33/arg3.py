def display_info(**data):
    for key, value in data.items():
        print(f"{key}:{value}")

display_info(nome=" Maria", idade=" 18", profissão=" Engenheira")