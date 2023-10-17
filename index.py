import db

# simulação de um cache 
application_in_memory = {}

# entrada do usuario 
numbers_of_users = int(input("Informe a quantidade de usuarios que desejar armazenar os resultados:"))


def Application():
    for i in range(numbers_of_users):
        name = input(f"Informe o nome do usuario-{i}:")
        if db.findByUsers(name):
            return 
        notes = int(input(f"Informe a quantidade de notas que desejar armazenar:"))
        if not "users" in application_in_memory: 
            application_in_memory["users"] = {}
        if not name in application_in_memory["users"]:
            application_in_memory["users"][name] = {}
        if not "grades" in application_in_memory["users"][name]: 
            application_in_memory["users"][name]["grades"] = ()
        for _ in range(notes): 
            notes_user = input(f"Me informe as notas de {name} nesses exemplos (e1_t2_p3_s4):")
            if not  application_in_memory["users"][name]["grades"]: 
                application_in_memory["users"][name]["grades"] = {}
                application_in_memory["users"][name]["grades"][notes_user[0]] = ()
            application_in_memory["users"][name]["grades"][notes_user[0]] = (notes_user)
    db.createUsers(application_in_memory["users"])


Application()