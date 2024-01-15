from xml.dom import ValidationErr
from fastapi import APIRouter, HTTPException, Response
from config.db import conn
from schemas.animal import animalEntity, animalesEntity
from models.animal import Animal
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

animal = APIRouter()

@animal.get("/animales")
def find_all_animales():
    animals = list(conn.animales.animal.find())
    return animalesEntity(animals)

@animal.get("/animales/{id}")
def find_animal(id: str):
    object_id = ObjectId(id)
    
    animal = conn.animales.animal.find_one({"_id": object_id})
    
    if animal:
        return animalEntity(animal)
    
    raise HTTPException(status_code=404, detail="Animal con id:" + id + " no existe")

@animal.post("/animales")
def create_animal(animal: Animal):
    try:
        new_animal = dict(animal)
        new_animal['fecha_nacimiento'] = animal.fecha_nacimiento.isoformat()

        id = conn.animales.animal.insert_one(new_animal).inserted_id

        animal_result = conn.animales.animal.find_one({"_id": id})

        if animal_result:
            return animalEntity(animal_result)

        raise HTTPException(status_code=500, detail="Error al crear el animal.")
    except ValidationErr as ve:
        error_message = ve.errors()[0]['msg'] if ve.errors() else "Error de validación"
        raise HTTPException(status_code=422, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")



@animal.put("/animales/{id}")
def update_animal(id: str, animal: Animal):
    try:
        conn.animales.animal.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre_animal": animal.nombre_animal,
                "fecha_nacimiento": animal.fecha_nacimiento.isoformat(),
                "edad": animal.edad,
                "especie": animal.especie,
                "habitat": animal.habitat,
            }}
        )

        updated_animal = conn.animales.animal.find_one({"_id": ObjectId(id)})

        if updated_animal:
            return animalEntity(updated_animal)

        raise HTTPException(status_code=404, detail=f"Animal con id:{id} no encontrado")
    
    except ValidationError as ve:
        raise HTTPException(status_code=422, detail=f"Error de validación: {ve.errors()}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


@animal.delete("/animales/{id}")
def delete_animal(id: str):
    conn.animales.animal.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return {"message": "Animal eliminado correctamente"}

