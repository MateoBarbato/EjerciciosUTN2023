from funciones import *


def menu():
    flagMenu = True
    while True:
        if(flagMenu):
            imprimirLista()
        numero = input('Elija entre las funciones:')

        if numero.isdigit():
            numero = int(numero)
            if numero <= 22 and numero >= 0:
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
            masAltoMasc(False)
        case 11:
            masAltoFem(False)
        case 12:
            masBajoMasc(False)
        case 13:
            masBajoFem(False)
        case 14:
            promedioMasc()
        case 15:
            promedioFem()
        case 16:
            minMaxGeneros()
        case 17:
            cantColorDePelo()
        case 18:
            cantColorDeOjos()
        case 19:
            tipoDeInteligencia()
        case 20:
            agruparPorOjos()
        case 21:
            agruparPorPelo()
        case 22:
            agruparPorInteligencia()
        case 0:
            salir_del_programa()
        case _:
            print("Opcion invalida. Ingrese un numero entre 0 y 18.")
    menu()