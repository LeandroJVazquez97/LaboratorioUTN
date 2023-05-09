from os import system

system("cls")

from biblioteca import *

# mostrar_menu_principal()

lista_pokemones = []
lista_pokemones = traer_datos_archivo()

# lista_cantidad_tipo(lista_pokemones, 'Habilidades')

listar_pokemones_tipo(lista_pokemones, 'Tipo')
