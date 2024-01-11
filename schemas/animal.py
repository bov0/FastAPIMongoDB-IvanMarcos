def animalEntity(item) -> dict:
    return {
        "id_animal": item["id_animal"],
        "nombre_animal": item["nombre_animal"],
        "fecha_nacimiento": item["fecha_nacimiento"],
        "edad": item["edad"],
        "id_especie": item["id_especie"],
        "id_habitat": item["id_habitat"]
    }

def animalesEntity(entity) -> list:
    return [animalEntity(item) for item in entity]