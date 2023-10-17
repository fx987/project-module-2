# Criando um cache em memoria para otimização de querys para o banco de dados
application_in_memory = {}


regex = "n não"

def Application():
    while True: 
        # Numero de candidatos que desejar armazenar os resultados
        numbers_of_users = int(input("Informe a quantidade de usuarios que desejar armazenar os resultados:"))
        # Loop de criação de usuarios
        for i in range(numbers_of_users):
            name = input(f"Informe o nome do usuario-{i}:")
            notes = int(input(f"Informe a quantidade de notas que desejar armazenar:"))
        
        # Caso o objeto não existir, apenas verficações de tratamento de erros
        if not "users" in application_in_memory: 
            application_in_memory["users"] = {}
        # Caso o objeto não existir, apenas verficações de tratamento de erros
        if not name in application_in_memory["users"]:
            application_in_memory["users"][name] = {}
        # Caso o objeto não existir, apenas verficações de tratamento de erros
        if not "grades" in application_in_memory["users"][name]: 
            application_in_memory["users"][name]["grades"] = ()
        # Geração de notas associada ao aluno 
        for _ in range(notes): 
            notes_user = input(f"Me informe as notas de {name} nesses exemplos (e1_t2_p3_s4):")
            # Caso o objeto não existir, apenas verficações de tratamento de erros
            if not  application_in_memory["users"][name]["grades"]: 
                application_in_memory["users"][name]["grades"] = {}
                application_in_memory["users"][name]["grades"]=  ()
            application_in_memory["users"][name]["grades"] = (notes_user,)
        # Envia ao futuro banco de dados novos usuarios
        createUsers(application_in_memory["users"])

        # Cria uma requisição que solicitar uma busca
        request = input("Desejar realizar uma busca?:")

        # Verificar se o usuario recusou a busca
        if not regex in request: 
            # Cria uma requisição que solicitar uma busca das notas no exemplo = e1_t2
            filterNotes = input("Me informe as notas minima que desejar analisar nesses exemplos (e1_t2_p3_s4):").split("_")
            filterr = findByNotes(filterNotes)
            # Verificar se encontrou um usuario
            if filterr != {}: 
                # Listar os usuarios
                for _,v in enumerate(filterr): 
                    print(f"-"*20)
                    print(f"Candidato {v} | Resultado: {filterr[v]}")
            # Verificar se desejar realizar uma nova busca
            request_return = input("Desejar realizar uma nova busca?")
            # Se caso ele nao quiser ele para o programa
            if regex in request_return: 
                break

        
# Iniciando a aplicação
Application()



###################################### utils #######################################


def createUsers(newDict:dict):
    application_in_memory["users"] = newDict

def findByNotes(tp: list) -> dict: 
    filterCandidates = {}
    for _,v in enumerate(application_in_memory["users"]): 
        if v:
            for n in application_in_memory["users"][v]["grades"]:
                for i in tp:
                    if (n[1]) >= (i[1]):
                        filterCandidates[v] = {
                            "notes": f"{i}"
                        }
    return filterCandidates

def updateGrades(name: str, nameUpd: str) -> any: 
    for _,v in enumerate(application_in_memory["users"]):
        if v["name"] == name: 
            application_in_memory["users"]["name"] = nameUpd 
    return False,"Usuario não encontrado."