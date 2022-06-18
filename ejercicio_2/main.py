import requests
from novela import Novela

url_books = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

http_rsp = requests.get(url_books)
novelas_rsp = http_rsp.json()

novelas = []

for novela in novelas_rsp:
    novelas.append(Novela(novela['name'], novela['city']))

def user_menu():
    print('Menú Novelas')

    while True:
        print('(1) Listar novelas')
        print('(2) Agregar novela')
        print('(3) Salir')

        option = input('>> ')

        if option == '1':
            for novela in novelas:
                print(novela)
        elif option == '2':
            print('Nueva novela')
            titulo = input('Título: ')
            origen = input('Origen: ')

            mi_novela = Novela(titulo, origen)
            novelas.append(mi_novela)

        elif option == '3':
            break
        else:
            print('Ingrese una opción válida')

user_menu()