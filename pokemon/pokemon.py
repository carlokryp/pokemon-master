import requests
import random
import queue
from threading import Thread


def get_pokemontypes():
    pokemontypes = {}
    url = "https://pokeapi.co/api/v2/type/"
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        resultados = payload.get("results", [])
        if resultados:
            i = 1
            for tipo in resultados:
                name = tipo["name"]
                pokemontypes[i] = name
                i += 1
        return pokemontypes
    else:
        return (print("No se obtuvieron los tipos, verificar url"))


def get_onetype(tipos):
    tipos = tipos
    ciclo = True
    op = None
    while ciclo:
        try:
            print (
                "Por favor tienes que legir una opc \n") \
                    if op is not None else ("")
            op = int(input(
                "Elige un numero para seleccionar tu tipo favorito: \
                     \n \n {} \n \t opcion: ".format(tipos)))
            ciclo = False if op in tipos else True
        except Exception as err:
            print (
                "Tienes que seleccionar una opcion mostrada.\
                     \n Error: ", err)
    return op


def get_pokemon_user(i):
    link = int(i)
    list_id = {}
    aux = 0
    lista = [None, None, None, None, None, None]
    url = "https://pokeapi.co/api/v2/type/{}".format(link)
    print (url)
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        pokemones = payload.get("pokemon", [])
        if (pokemones):
            for pokemon in pokemones:
                id = (pokemon["pokemon"]["url"]).split("/")[-2]
                list_id[int(id)] = pokemon["pokemon"]["name"]
                print (id, pokemon["pokemon"]["name"])
    print ("\n Para formar tu equipo, selecciona el ID de 6 pokemones")
    while (aux < 6):
        try:
            op = int(input("Elige un numero para seleccionar tu pokemon: \t "))
            if (op in list_id):
                lista[aux] = op
                aux += 1
            else:
                print ("Tienes que elegir un pokemon de la lista ")

        except Exception as err:
                print ("Tienes que seleccionar una opcion mostrada.\
                     \n Error: ", err)
    print("Seleccionando ataques para: ")
    for i in range(6):
        print(list_id[lista[i]])

    return (__ataques(lista))


def __ataques(lista):
    que = queue.Queue()
    threads_list = list()
    ataques = {}
    equipo = {}
    for i in range(2):
        t = Thread(target=__cuatroataques, args=(lista, ataques, i, que))
        t2 = Thread(target=__cuatroataques, args=(lista, ataques, i+2, que))
        t3 = Thread(target=__cuatroataques, args=(lista, ataques, i+4 que))
        t.start()
        t2.start()
        t3.start()
        threads_list.append(t)
        threads_list.append(t2)
        threads_list.append(t3)
    for hilo in threads_list:
        hilo.join()
    while not que.empty():
        result = que.get()
        equipo[result[0]] = result[1:]
    return (equipo)


def __cuatroataques(lista, ataques, i, que):
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(lista[i])
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        moves = payload.get("moves", [])
        j = 0
        for move in moves:
            ataques[j] = move["move"]["name"]
            j += 1
        equipo = {}
        lista_aux = []
        lista_aux.append(payload.get("name"))
        lista_aux.append(random.sample(list(ataques.values()), 4))
        equipo = lista_aux
        que.put(equipo)
    return equipo
