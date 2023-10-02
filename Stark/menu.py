from funciones import *


def menu():
    flagMenu = True
    while True:
        if(flagMenu):
            imprimirLista()
        numero = input('Elija entre las funciones:')

        if numero.isdigit():
            numero = int(numero)
            if numero <= 18 and numero >= 0:
                break
            else:
                flagMenu=False
                print("Opcion invalida. Ingrese un numero entre 0 y 18.")
        else:
            print("Opcion invalida. Ingrese un numero valido.")

    match numero:
        case 1:
            nombresSuperheroe()
        case 2:
            nombreyAltura()
        case 3:
            heroeMasAlto()
        case 4:
            heroeMasBajo(False)
        case 5:
            alturaPromedio()
        case 6:
            minMax()
        case 7:
            minMaxPeso()
        case 8:
            superHeroeMasc()
        case 9:
            superHeroeFem()
        case 10:
            masAltoMasc()
        case 11:
            masAltoFem()
        case 12:
            masBajoMasc()
        case 13:
            masBajoFem()
        case 14:
            promedioMasc()
        case 15:
            promedioFem()
        case 16:
            minMaxGeneros()
        case 0:
            salir_del_programa()
        case _:
            print("Opcion invalida. Ingrese un numero entre 0 y 18.")
    menu()