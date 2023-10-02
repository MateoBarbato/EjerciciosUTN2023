import os
from data_stark import lista_personajes


listaOpciones= ['1)Imprimir por nombre',
                '2)Imprimir por nombre y altura',
                '3)Superheroe mas alto',
                '4)Superheroe mas bajo',
                '5)Altura promedio',
                '6)Nombre del superheroe Max y Min',
                '7)SuperHereo mas y menos pesado',
                '8)Heroes (M)',
                '9)Heroes (F)',
                '10)SuperHereo mas alto (M)',
                '11)SuperHereo mas alto (F)',
                '12)SuperHereo mas bajo (M)',
                '13)SuperHereo mas bajo (F)',
                '14)Promedio Altura (M)',
                '15)Promedio Altura (F)',
                '16)MinMax por Genero',
                '17)Cantidad de color de pelo',
                '18)Cantidad de color de ojos',
                '19)Cantidad de color de inteligencia',
                '20)Agrupar por ojos',
                '21)Agrupar por pelo',
                '22)Agrupar por inteligencia',
                '0)Cerrar y salir']
def imprimirLista():
    
    """
    Imprime el menu de opciones
    """
    print("<============ Menu de funciones ===========>")
    for opcion in listaOpciones:
        print(f'{opcion}')

def nombresSuperheroe():
    limpiarConsola()
    print('Nombre:')
    # print(f'Nombre:{lista_personajes[0]['nombre']}')
    for heroe in lista_personajes:
        print(f"--> {heroe.get('nombre')}")

def nombreyAltura():
    limpiarConsola()
    print('Nombre y altura:')
    for heroe in lista_personajes:
        print(f"--> {heroe.get('nombre')}, {heroe.get('altura')} cm")

def heroeMasAlto(returning):
    limpiarConsola()
    maximo = 0
    maximoNombre= None
    for heroe in lista_personajes:
        altura = int(float(heroe.get('altura')))
        if(maximo == 0):
            maximo = int(float(heroe.get('altura')))
            maximoNombre = heroe.get('nombre')
        if(altura > maximo):
            maximoNombre = heroe.get('nombre')
            maximo = int(float(heroe.get('altura')))
    print(f'Altura maxima: {maximoNombre} con {maximo} cm')
    if(returning):
        return [maximo, maximoNombre]

def heroeMasBajo(returning):
    limpiarConsola()
    minimo = 0
    minimoNombre= None
    for heroe in lista_personajes:
        altura = int(float(heroe.get('altura')))
        if(minimo == 0):
            minimo = int(float(heroe.get('altura')))
            minimoNombre = heroe.get('nombre')
        if(altura < minimo):
            minimoNombre = heroe.get('nombre')
            minimo = int(float(heroe.get('altura')))
    print(f'Altura maxima: {minimoNombre} con {minimo} cm')
    if(returning):
        return [minimo, minimoNombre]

def minMax():
    limpiarConsola()
    masBajo = heroeMasBajo(True)
    masAlto = heroeMasAlto(True)
    print(f'El heroe mas bajo: {masBajo[1]} midiendo {masBajo[0]} cm')
    print(f'El heroe mas alto: {masAlto[1]} midiendo {masAlto[0]} cm')

def alturaPromedio():
    limpiarConsola()
    total = 0

    for heroe in lista_personajes:
        total = total + int(float(heroe.get('altura')))
    promedio = total / len(lista_personajes)
    print(f'La altura promedio de los heroes es de : {promedio}')

def minMaxPeso():
    limpiarConsola()
    minimoPeso = 0
    minimoPesoNombre= None
    maximoPeso = 0
    maximoPesoNombre= None
    for heroe in lista_personajes:
        peso = int(float(heroe.get('peso')))
        if(minimoPeso == 0):
            minimoPeso = int(float(heroe.get('peso')))
            minimoPesoNombre = heroe.get('nombre')
        if(peso < minimoPeso):
            minimoPesoNombre = heroe.get('nombre')
            minimoPeso = int(float(heroe.get('peso')))

    
    for heroe in lista_personajes:
        pesoMax = int(float(heroe.get('peso')))
        if(maximoPeso == 0):
            maximoPeso = int(float(heroe.get('peso')))
            maximoPesoNombre = heroe.get('nombre')
        if(pesoMax > maximoPeso):
            maximoPesoNombre = heroe.get('nombre')
            maximoPeso = int(float(heroe.get('peso')))


    print(f'Peso maximo: {maximoPesoNombre} con {maximoPeso} kg')
    print(f'Peso minimo: {minimoPesoNombre} con {minimoPeso} kg')


def superHeroeMasc():
    limpiarConsola()
    for heroe in lista_personajes:
        if heroe.get('genero') == 'M':
            print(heroe.get('nombre'))

def superHeroeFem():
    limpiarConsola()
    for heroe in lista_personajes:
        if heroe.get('genero') == 'F':
            print(heroe.get('nombre'))

def masAltoMasc(returning):
    limpiarConsola()
    maximo = 0
    maximoNombre= None
    for heroe in lista_personajes:
        if heroe.get('genero') == 'M':
            altura = int(float(heroe.get('altura')))
            if(maximo == 0):
                maximo = int(float(heroe.get('altura')))
                maximoNombre = heroe.get('nombre')
            if(altura > maximo):
                maximoNombre = heroe.get('nombre')
                maximo = int(float(heroe.get('altura')))
    if(returning):
        return [maximo, maximoNombre]
    else:
        print(f'Altura maxima (M): {maximoNombre} con {maximo} cm')


def masAltoFem(returning):
    limpiarConsola()
    maximo = 0
    maximoNombre= None
    for heroe in lista_personajes:
        if heroe.get('genero') == 'F':
            altura = int(float(heroe.get('altura')))
            if(maximo == 0):
                maximo = int(float(heroe.get('altura')))
                maximoNombre = heroe.get('nombre')
            if(altura > maximo):
                maximoNombre = heroe.get('nombre')
                maximo = int(float(heroe.get('altura')))
    if(returning):
        return [maximo, maximoNombre]
    else:
        print(f'Altura maxima (F): {maximoNombre} con {maximo} cm')

def masBajoMasc(returning):
    limpiarConsola()
    minimo = 0
    minimoNombre= None
    for heroe in lista_personajes:
        if heroe.get('genero') == 'M':
            altura = int(float(heroe.get('altura')))
            if(minimo == 0):
                minimo = int(float(heroe.get('altura')))
                minimoNombre = heroe.get('nombre')
            if(altura < minimo):
                minimoNombre = heroe.get('nombre')
                minimo = int(float(heroe.get('altura')))
    if(returning):
        return [minimo, minimoNombre]
    else:
        print(f'Altura minima (M): {minimoNombre} con {minimo} cm')

def masBajoFem(returning):
    limpiarConsola()
    minimo = 0
    minimoNombre= None
    for heroe in lista_personajes:
        if heroe.get('genero') == 'F':
            altura = int(float(heroe.get('altura')))
            if(minimo == 0):
                minimo = int(float(heroe.get('altura')))
                minimoNombre = heroe.get('nombre')
            if(altura < minimo):
                minimoNombre = heroe.get('nombre')
                minimo = int(float(heroe.get('altura')))
    if(returning):
        return [minimo, minimoNombre]
    else:
        print(f'Altura minima (F): {minimoNombre} con {minimo} cm')

def promedioMasc():
    limpiarConsola()
    total = 0
    contador = 0
    for heroe in lista_personajes:
        if heroe.get('genero') == 'M':
            contador = contador + 1
            total = total + int(float(heroe.get('altura')))
            promedio = total / contador
    print(f'La altura promedio de los heroes (M) es de : {promedio}')

def promedioFem():
    limpiarConsola()
    total = 0
    contador = 0
    for heroe in lista_personajes:
        if heroe.get('genero') == 'F':
            contador = contador + 1
            total = total + int(float(heroe.get('altura')))
            promedio = total / contador
    print(f'La altura promedio de los heroes (F) es de : {promedio}')

def minMaxGeneros():
    limpiarConsola()
    bajoMasc = masBajoMasc(True)
    bajoFem = masBajoFem(True)
    altoFem = masAltoFem(True)
    altoMasc = masAltoMasc(True)
    print(f'El heroe mas bajo (M): {bajoMasc[1]} midiendo {bajoMasc[0]} cm')
    print(f'El heroe mas bajo (F): {bajoFem[1]} midiendo {bajoFem[0]} cm')

    print(f'El heroe mas alto (M): {altoMasc[1]} midiendo {altoMasc[0]} cm')
    print(f'El heroe mas alto (F): {altoFem[1]} midiendo {altoFem[0]} cm')

def cantColorDePelo():
    colorDePeloDict = {}
    for personaje in lista_personajes:
        
        color_pelo = personaje["color_pelo"].lower()
        
        if color_pelo in colorDePeloDict :
            colorDePeloDict[color_pelo] += 1
        else:
            colorDePeloDict[color_pelo] = 1
    
    for color in colorDePeloDict:
        print(f"Cantidad de {color}: {colorDePeloDict.get(color)}")
     
def cantColorDeOjos():
    colorDeOjosDict = {}
    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"].lower()
        if color_ojos in colorDeOjosDict :
            colorDeOjosDict[color_ojos] += 1
        else:
            colorDeOjosDict[color_ojos] = 1
    
    for color in colorDeOjosDict:
        print(f"Cantidad de {color}: {colorDeOjosDict.get(color)}") 
def tipoDeInteligencia():
    tiposdeInt = {}
    for personaje in lista_personajes:
        tipodeInt = personaje["inteligencia"].lower()
        if '' == tipodeInt:
            tiposdeInt['No Tiene']= 1
        else:
            if tipodeInt in tiposdeInt :
                tiposdeInt[tipodeInt] += 1
            else:
                tiposdeInt[tipodeInt] = 1
    
    for intel in tiposdeInt:
        print(f"Cantidad de {intel}: {tiposdeInt.get(intel)}") 
    

def agruparPorOjos():
    pass
def agruparPorPelo():
    pass
def agruparPorInteligencia():
   pass

def limpiarConsola():
    import os
    os.system('cls||clear')

def salir_del_programa():
    limpiarConsola()
    print("Saliendo del programa...")
    exit()