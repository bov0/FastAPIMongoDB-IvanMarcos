def animalEntity(item) -> dict:
    return {
        "id_animal": str(item["_id"]),
        "nombre_animal": item["nombre_animal"],
        "fecha_nacimiento": item["fecha_nacimiento"],
        "edad": item["edad"],
        "especie": item["especie"],
        "habitat": item["habitat"]
    }

def animalesEntity(entity) -> list:
    return [animalEntity(item) for item in entity]