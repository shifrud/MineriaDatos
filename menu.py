# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:43:04 2016

@author: Gerardo Lara Rojas
"""
import temp#importamos nuestro otro programa
import knn#importamos el progrmama knn para clasificacion

opcion=0#se asigna el valor de 0 para trabajar con la imagen

while(opcion!=3):
    print("Selecciona una opcion ")#impresion de pantalla
    opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))#Menú de opciones que contiene la variable opcion de tipo int que servira para evaluar lo que hara el programa

    if(opcion<1 or opcion>3):#la variable opcion es validada con la finalidad de el usuario solo pueda saleccionar un rango de numero que debera estar entre el 1 y el 3
        print("Error")#si el numero seleccionado por el usuario no se encuentra dentro de rango 1:3 se mostrara en pantalla un mesaneje de error
    if (opcion==1):#se evalalua que el numero ingresado por el usuario sea igual a 1
        temp.creardataset()#si el numero ingresado por el usuario es igual entonce invocamos al metodo Dataset y a la funcion dataset con la finalidad de generar un nuevo dataset
    if (opcion==2):#se evalua si el numero ingresado por el usuario es igual a 2 
        knn.instancias_de_la_clase()#se aplica la funcion de clasificacion del metodo KNN
        
print("Adios")#mensaje de despedida