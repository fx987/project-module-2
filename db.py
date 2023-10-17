applications = {}

def createUsers(newDict:dict):
    applications["users"] = newDict

def findByAll() -> dict: 
    for i in applications["users"]: 
        return i

def findByUsers(name: str) -> list[any]:
    if "users" in applications: 
        for _,v in enumerate(applications["users"]):
            if name == v["name"]: 
                return v["grades"],True
    return None


def updateGrades(name: str, nameUpd: str) -> any: 
    for _,v in enumerate(applications["users"]):
        if v["name"] == name: 
            applications["users"]["name"] = nameUpd 
    return False,"Usuario não encontrado."