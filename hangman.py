import random
import os

def run():
    intentos=5
    acierto=0
    lista=[]
    final=""

    #Abriendo el archivo
    with open('C:/Users/Ronald/OneDrive - Universidad de San Buenaventura Seccional Medellin/Certificaciones/Platzi/Curso Intermedio de Python/archivos/data.txt',"r",encoding="utf-8")as f:
        for i in f:
            lista.append(i.rstrip("\n"))
    
    #Obtenido palabra random
    palabra=random.choice(lista)
    
    adivina = ["_" for i in palabra ]
    print(""" 
        Bienvenido/a al juego del ahorcado 
        la palabra que debes adivinar es """  + "_ "*len(palabra)
        +"Tienes " + str(intentos)+ " intentos")
    while(True):

        letra=input("Ingresa una letra: ").lower()
        if(len(letra)>=2 or letra.isalpha==False):
            letra=""
            print(" Has ingresado un caracter inválido")
            continue

        for count, i in enumerate(palabra):
            if letra == i:
                adivina[count]=letra
                acierto+=1
        print("acertaste " + str(acierto) + " veces la letra " + letra)
        acierto=0
        if letra not in palabra:
            intentos -= 1
            print("fallaste te restan "+ str(intentos)+ " intentos")
        
        for i in adivina:
            print(i, end=" ")
            final += i
        if final == palabra:
            print("Has ganado, la palabra correcta es " + final)
            break
        if intentos == 0:
            print("Has perdido, mejor suerte la próxima la palabra correcta era "+ palabra)
            break
        final=""        

if __name__ == "__main__":
    run()