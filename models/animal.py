from typing import Optional
from pydantic import BaseModel
from datetime import date

class Animal(BaseModel):
    id_animal: Optional[int]
    nombre_animal: str
    fecha_nacimiento: date
    edad: int
    id_especie: int
    id_habitat: int
