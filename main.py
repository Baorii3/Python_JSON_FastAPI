from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Alumne(BaseModel):
    nom: str
    cognom: str
    dia: int
    mes: int
    any: int
    email: str
    feina: bool
    curs: str

# Funció de llegir un fitxer   
def llegir_fixer():
    # Obrim l'arxiua amb per lectura
    fitxer = open ("alumnes.json", "r")
    # Llegim el fitxer a un String
    a = fitxer.read() 
    # Ho pasem a un dicc
    alumnes = json.loads(a)
     # Ho tanquem
    fitxer.close()
    return alumnes

# Funcio per a obtenir la id mes gran en el fitxer json
def obtenir_id(alumnes):
    if not alumnes:
        return 1
    else:
        id = []
        for alumne in alumnes:
            # añadimos el id de todos
            id.append(alumne["id"])
        # Devolvemos el id mas alto
        return max(id)+1

# Llegim el fitxer per a tenir dades
alumnes = llegir_fixer()

# Si no posem res després del http://127.0.0.1:8000/docs
@app.get("/")
def index():
    return "Institut TIC de Barcelona"

# Si fem el get de alumnes sortirà el total de alumnes que hi ha
@app.get("/alumnes")
def llistar_alumnes():
    return f"Alumnes en total: {len(alumnes)}"

# Si troba el alumne buscat per id hauràn de sortir les dades d'aquest
@app.get("/id/{numero}")
def obtenir_alumne(id: int):
    for alumne in alumnes:
        # Busquem per id
        if alumne["id"] == id:
            return alumne
        
    return "L'alumne no existeix"

# Si troba el alumne buscat per id haurà de treure-ho de la taula 
@app.delete("/del/{numero}")
def esborrar_alumne(id: int):
    for alumne in alumnes:
        # Busquem per id
        if alumne["id"] == id:
            # Treiem el 
            alumnes.remove(alumne)
            return "Alumne eliminat"
        
    return "L'alumne no existeix"

# Afegirem un nou alumne amb les dades que es posin
@app.post("/alumne")
def crear_alumne(nou: Alumne):
    # Fem un dicc per afegir les dades del nou Alumne
    # La id la posara automatica
    dic = {"id":obtenir_id(alumnes), "nom":nou.nom, "cognom":nou.cognom, "data":{"dia":nou.dia, "mes":nou.mes, "any":nou.any}, "email":nou.email, "feina":nou.feina, "curs":nou.curs}
    # Afegim el dic a alumnes
    alumnes.append(dic)
    return "L'alumne s'ha inserit correctament"

