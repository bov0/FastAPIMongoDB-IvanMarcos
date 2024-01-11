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
    new_animal = dict(animal)
    
    new_animal['fecha_nacimiento'] = animal.fecha_nacimiento.isoformat()

    id = conn.animales.animal.insert_one(new_animal).inserted_id

    animal = conn.animales.animal.find_one({"_id": id})

    return animalEntity(animal)

@animal.put("/animales/{id}")
def update_animal(id: str, animal: Animal):
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
    return animalEntity(conn.animales.animal.find_one({"_id": ObjectId(id)}))

@animal.delete("/animales/{id}")
def delete_animal(id: str):
    conn.animales.animal.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return {"message": "Animal eliminado correctamente"}

