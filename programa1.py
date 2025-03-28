# imports
import os
import json
import time

# Funció que mostra el menu
def menu():
    # Netejem la pantalla
    os.system("cls")

    print("GESTIO D'ALUMNES")
    print("-------------")
    print("1. Mostrar llistat dels alumnes")
    print("2. Afegir un alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    print("5. Desar a fitxer")
    print("6. Llegir fitxer")
    print("7. Sortir")
    num = input("> ")

    # comprovamos que sea int
    try:
        num = int(num)
    except:
        print("Posa un numero")
    return num

# Funcio per a obtenir la id mes gran en el fitxer json
def obtenir_id(alumnes):
    # Netejem la pantalla
    os.system("cls")

    if not alumnes:
        return 1
    else:
        id = []
        for alumne in alumnes:
            # añadimos el id de todos
            id.append(alumne["id"])
        # Devolvemos el id mas alto
        return max(id)+1

# Funcion para incrementar contador
def incrementa_cont():
    global cont
    cont += 1

# Funcio que mostra un llistat de tots els alumnes
def mostra_alumnes(alumnes):
    # Netejem la pantalla
    os.system("cls")

    print("MOSTRAR ALUMNES")
    print("---------------")
    print("{")
    for alumne in alumnes:
        print(f"id:{alumne["id"]}, nom:{alumne["nom"]}, cognom:{alumne["cognom"]}")
    
    print("}")
    input(("INPUT per tornar: "))

# funcio per afegir un alumne al dic
def afegir_alumnes(alumnes):
    # Netejem la pantalla
    os.system("cls")

    print("AFEGIR ALUMNE")
    print("-------------")
    while True: 
        # Agafem les dades que volem
        global cont
        id = cont
        nom = input("nom: ")
        cognom = input("cognom: ")
        dia = int(input("dia: "))
        mes = int(input("mes: "))
        any = int(input("any: "))
        email = input("email: ")
        feina = input("feina(si/no): ").strip().lower() == "si"
        curs = input("curs: ")

        # Ara creem el nou alumne amb les dades de abans
        alumne = {
            "id":id,
            "nom":nom,
            "cognom":cognom,
            "data": {"dia":dia,"mes":mes,"any":any},
            "email":email,
            "feina":feina,
            "curs":curs
        }

        # Ara afegim el nou alumne al dic
        alumnes.append(alumne)
        print("Nou alumne afegit correctament")

        # Incrementem el contador per a que el id sigui automatic
        incrementa_cont()

        # Mirem si vol afegir altre
        if input("Vols afegir una altre? (si/no): ").strip().lower() == "no":
            break

# Funcio per veure un unic alumne al seu id
def veure_alumne(alumnes):
    while True:   
        # Netejem la pantalla
        os.system("cls")
        print("VEURE ALUMNE")
        print("------------")
        id = int(input("Posa la id del alumne que vulguis: "))
        # Busquem en un bucle si es troba la id
        for alumne in alumnes:
            if id == alumne["id"]:
                # Si la troba sortirà per pantalla
                print(f"id: {alumne['id']}")
                print(f"nom: {alumne['nom']}")
                print(f"cognom: {alumne['cognom']}")
                print(f"data de naixement: {alumne['data']}")
                print(f"email: {alumne['email']}")
                print(f"feina: {'Sí' if alumne['feina'] else 'No'}")
                print(f"curs: {alumne['curs']}")
                break 
        # Si no surt ho dirà
        else:
            print("Alumne no trobat")

        # Preguntem si vol buscar un altre
        if input("Vols afegir una altre? (si/no): ").strip().lower() != "si":
            break


# Funcio per esborrar un alumne pel seu id
def esborrar_alumne(alumnes):
    while True:   
        # Netejem la pantalla
        os.system("cls")
        print("VEURE ALUMNE")
        print("------------")
        id = int(input("Posa la id del alumne que vulguis: "))
        # Busquem en un bucle si es troba la id
        for alumne in alumnes:
            if id == alumne["id"]:
                # Si la troba sortirà per pantalla
                alumnes.remove(alumne)
                print("Alumne esborrat correctament")
                break 
        # Si no surt ho dirà
        else:
            print("Alumne no trobat")

        # Preguntem si vol buscar un altre
        if input("Vols esborrar una altre? (si/no): ").strip().lower() != "si":
            break

# Funcio per desar a fixter el nostre dic. El fitxer s'anomenada alumnes.json
def desar_json(alumnes):
    # Netejem la pantalla
    os.system("cls")
    print("DESAR JSON")
    print("----------")
    # Obrim l'arxiua amb per escriure
    fitxer = open ("alumnes.json","w")
    # Passem el diccionari a string
    diccString = json.dumps(alumnes)
    # Ho escrivim al fitxer
    fitxer.write(diccString)
    # Ho tanquem
    fitxer.close

    print("JSON desat correctament")
    input(("INPUT per tornar: "))    
    return

# Funcio per llegit un fitxer json anomenat alumnes.json
def llegir_fixer():
    # Netejem la pantalla
    os.system("cls")

    print("DESAR JSON")
    print("----------")

    # Obrim l'arxiua amb per lectura
    fitxer = open ("alumnes.json", "r")
    # Llegim el fitxer a un String
    a = fitxer.read() 
    # Ho pasem a un dicc
    alumnes = json.loads(a)
     # Ho tanquem
    fitxer.close()
        
    print("JSON carregat correctament")
    return alumnes

# Funcio per sortir
def sortir():
    exit()

# On es trucaran les funcions
alumnes = llegir_fixer()

cont = obtenir_id(alumnes)
while True:
    num = menu()
    if num == 1:
        mostra_alumnes(alumnes)
    elif num == 2:
        afegir_alumnes(alumnes)
    elif num == 3:
        veure_alumne(alumnes)
    elif num == 4:
        esborrar_alumne(alumnes)
    elif num == 5:
        desar_json(alumnes)
    elif num == 6:
        alumnes = llegir_fixer()
    elif num == 7:
        sortir()
    else:
        if isinstance(num, int):
            print("No hi ha aquella opció")
        time.sleep(1)
    