import re

"""
Brief: Recibe un valor y retorna si es una opcion valida
    Parameters:
        opcion: recibe un input y lo convierte a enteroo
    Return: Si es una opcion valida retorna True, sino False
"""
def validar_opcion(opcion:str):
    if(opcion.isdigit() == True):
        opcion = int(opcion)
        if(1 <= opcion or opcion <= 8):
            return True
        else:
            return False
    else:
        return False

"""
Brief: Imprime menu y valida la opcion ingresada
    Parameters:
        No recibe
    Return: No retorna, solo ejecuta el codigo
"""
def mostrar_menu_principal():
    menu = """MENU:
    1_Traer datos desde archivo
    2_Listar cantidad por tipo
    3_Listar pokemones por tipo
    4_Listar pokemones por habilidad 
    5_Listar pokemones ordenados
    6_Guardar Json
    7_Leer Json

    8_Salir del programa\n"""

    print(menu)

    bandera = False

    while(bandera == False):
        opcion_input = input("")

        bandera = validar_opcion(opcion_input)

        if(bandera == False):
            print("Re-ingrese una opcion valida: ")
        else:
            match(opcion_input):
                case 1:
                    traer_datos_archivo()
                case 2:
                    lista_cantidad_tipo()


"""
Brief: Recibe una lista y un indice a eliminar de la misma
    Parameters:
        lista: recibe una lista
        indice: recibe el numero de indice
    Return: Retorna lista con el numero de indice eliminado
"""
def eliminar_elemento_lista(lista_original:list, indice:int) -> list:
    lista_original.pop(indice)

    return lista_original

"""
Brief: Se recibe una clave con varios valores y se los genera en lista con el metodo split
    Parameters:
        lista: lista de pokemones
        separador: string de division
        clave: key a analizar
    Return: Retorna la lista de pokemones
"""
def generar_lista(lista:list, separador:str, clave:str) -> list:
    for linea in lista:
        registro = re.split(separador, linea[clave])

        linea[clave] = registro

    return lista

"""
Brief: Se trae datos de pokemones de un archivo csv y se guardan en una lista 
    Parameters:
        No recibe parametros
    Return: Retorna una lista formateada
"""
def traer_datos_archivo():
    lista_retorno = []
    path = "pokemones.csv"

    archivo = open(path, "r")
    for linea in archivo:
        registro = re.split(";", linea)
        pokemon = {}
        pokemon['Pokedex'] = registro[0]
        pokemon['Nombre'] = registro[1]
        pokemon['Tipo'] = registro[2]
        pokemon['Poder_de_Ataque'] = registro[3]
        pokemon['Poder_de_Defensa'] = registro[4]
        pokemon['Habilidades'] = registro[5]
        lista_retorno.append(pokemon)

    archivo.close()

    lista_retorno = eliminar_elemento_lista(lista_retorno, 0)
    lista_retorno = generar_lista(lista_retorno, "/", "Tipo") 
    lista_retorno = generar_lista(lista_retorno, "\|\*\|", "Habilidades")
    
    return lista_retorno

"""
Brief: toma una lista de pokemones y mediante varios for anidados los lista por cantidad  
    Parameters:
        lista_pokemones: toma la lista de pokemones y los agrupa por su tipo
        clave: clave de la lista para trabajar 
    Return: No retorna - imprime la cantidad de pokemones que tiene cada clave
"""
def lista_cantidad_tipo(lista_pokemones:list, clave:str):
    lista = []
    lista_seteada = []

    for pokemon in lista_pokemones:
        for valores in pokemon[clave]:
            valores = re.sub(r'\n+', '', valores)
            
            lista.append(valores)

    lista_seteada = set(lista)

    for clave_seteados in lista_seteada:
        contador = 0 
        for clave_valor in lista:
            if(clave_seteados == clave_valor):
                contador = contador + 1

        print(f"La cantidad de pokemones de {clave} {clave_seteados} es: {contador}")

# 3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
# de ataque de cada pokemon que corresponde a ese tipo.

def listar_pokemones_tipo(lista_pokemones:list, clave:str):
    lista = []
    lista_seteada = []

    for pokemon in lista_pokemones:
        for valores in pokemon[clave]:
            valores = re.sub(r'\n+', '', valores)
            
            lista.append(valores)

    lista_seteada = set(lista)

    for pokemon in lista_pokemones:
        for valor in lista_seteada:
            if(valor == pokemon[clave]):
                print("Si")