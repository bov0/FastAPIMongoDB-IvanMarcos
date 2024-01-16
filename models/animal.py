from pydantic import BaseModel
from datetime import date

class Animal(BaseModel):
    nombre_animal: str
    fecha_nacimiento: date
    edad: int
    especie: str
    habitat: str