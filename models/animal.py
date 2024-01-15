from pydantic import BaseModel
from datetime import date
from pydantic import validator, ValidationError
from fastapi import HTTPException

class Animal(BaseModel):
    nombre_animal: str
    fecha_nacimiento: date
    edad: int
    especie: str
    habitat: str

    @validator("edad")
    def validate_edad(value):
        if value < 0:
            raise ValueError("La edad no puede ser menor que cero")
        return value

    @validator("nombre_animal", "especie", "habitat")
    def validate_string_no_numbers(value):
        if any(char.isdigit() for char in value):
            raise ValueError("Los nombres no pueden contener números")
        return value