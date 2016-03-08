import matplotlib.image as mpimg#libreria usada para trbajar con la imgane
import os#libreria para trabajar con el data set
import csv#extendcion de el resultado


#Nombre:Area
#Descripcion:saca el area de las imagenes 
#Argumentos:img que es la imagen
#Retorno: la area de la imagen
def Area(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    area=filas*columnas#son multiplicadas para sacar el area de la imagen
    return area#regresa la variable area que es la que usaremos
    
#Nombre:tamaño
#Descripcion:funcion que saca el tamaño de la imgagen en pixeles
#Argumentos:img que es la imagen
#Retorno: retorna el tamaño
def Tamaño(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    tamaño=filas/columnas#son divididas para 
    return tamaño#regresa el tamaño

#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador
def Linea1Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=columnas/2#dividimos el tamaño medio de las columnas entre dos
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar 
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos 
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print("linea 1 horizontal",cortador)
    return cortador, contadorblanco#retorna el cortador y contador


#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador
def Linea2Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar   
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos  
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
   # print(cortador)
    return cortador, contadorblanco#retorna el cortador y contador


#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador blanco y el cortador
def Linea3Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=columnas/2#dividimos el tamaño medio de las columnas entre dos
    columnas=columnas*3#se multiplica por 3 para que la linea este a 3 cuartos de la imagen
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar     
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos   
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print(cortador)
    return cortador,contadorblanco#retorna el cortador y contador

#Nombre:Linea1vertical
#Descripcion:trasa una linea a una cuarta parte
#Argumentos:img es a variable donde se cuarda la imgen
#Retorno:retorna el contador blanco y el cortador
def Linea1Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=filas/2#dividimos el tamaño medio de las filas entre dos    
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar       
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos     
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print("linea 1 vertical",cortador)
    return cortador, contadorblanco#retorna el cortador y contador
    

#Nombre:Linea2Vertical
#Descripcion:trasa una linea a mitad de la imgen
#Argumentos:img es a variable donde se cuarda la imgen
#Retorno:retorna el contador blanco y el cortador
def Linea2Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar         
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos     
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#condicion if para contar los pixeles blancos
    #print("linea 2 vertical",cortador)
    return cortador, contadorblanco#retorna el cortador y contador

#Nombre:Buscar archivos
#Descripcion:busca los archivos de un fichero
#Argumentos:ruta
#Retorno:retorna el contador blanco y el cortador    
def BuscarArchivos(ruta): 
    path =ruta
    #Lista vacia para incluir los ficheros
    lstFiles = []
 
     #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
#Crea una lista de los ficheros png que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:#ciclo usado para recorrer todos los archivos
        for fichero in files:#recorrera de fichechero en cichero los archivos
            (nombreFichero, extension) = os.path.splitext(fichero)#en caso de cso de encontrar archivos
            if(extension == ".png"):#si la extension del archivo es .png
                lstFiles.append(nombreFichero+extension)#se guarda el nombre del fichero con su extencion
                        
                        
    return lstFiles#retorna la imagen y extencion

    
#Nombre:Linea3vertical
#Descripcion:saca la 3 lineaen la imagen
#Argumentos:img nombre la variable que guarda la imgaen
#Retorno:contador blanco y cortador
def Linea3Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=filas/2#dividimos el tamaño medio de las filas entre dos    
    filas=filas*3#multiplicamos por 3 las filas para obtener 3 cuartos
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar         
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1 #se le va aumentando un uno para tener los cortes optenidos       
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#se le va aumentando un uno para tener los blancos optenidos       
   # print("Linea 3 vertical",cortador)
    return cortador,contadorblanco#retorna el cortador y contador


#Nombre:Creardataset
#DescripcionCrea el data set con todos los archivos
#Argumentos:null
#Retorna: la salida que tiene los datos
def creardataset():
    ruta='prueba/'#asignamos el nombre de la carpeta a la ruta
    archivo= open('resultado.csv', 'w', newline='')#abrimos el dataset y lo guardamos en archivo
    salida = csv.writer(archivo)#asignamos  una salida con extenxion csv
    numero=0#inicializamos numero
    for i in range(10):#se asigna un 10 por ser el numero de carpetasexistentes
        print("trabajando data set caracteristica del: "+str(i))#se imprime el msj de en que numero de carpeta va
        ruta=ruta+str(i)#se va asignando la ruta de cada una de las carpetas la caprta 10
        ls=BuscarArchivos(ruta)#se asgina la busqueda de los archivos
        
        
        for j in range(0,len(ls)):#se recorrera asta terminar los archivos dentro de las carpetas
            numero+=1#se agrega una variable que sera la contadora de las instancias
            rutaimagen=ruta+'/'+ls[j]#se asigna el contednido de las carpetas
            img=mpimg.imread(rutaimagen)#Ni idea de que pase aca
            caracteristica1=Linea1Horizontal(img)#obtenemos la caracteristica1     
            caracteristica2=Linea2Horizontal(img)#obtenemos la caracteristica2
            caracteristica3=Linea3Horizontal(img)##obtenemos la caracteristica3
            caracteristica4=Linea1Vertical(img)#obtenemos la caracteristica4
            caracteristica5=Linea2Vertical(img)#obtenemos la caracteristica5
            caracteristica6=Linea3Vertical(img)#obtenemos la caracteristica6
            caracteristica7=Area(img)#obtenemos la caracteristica7
            caracteristica8=Tamaño(img)#obtenemos la caracteristica8
            #la salida obtenida sera los valores guardados en nuestras caracteristticas al contener dos valores se asigna 0 que es el primer valor y 1 sienfo el segundo valor
            salida.writerow([caracteristica1[0],caracteristica1[1],caracteristica2[0],caracteristica2[1],caracteristica3[0],caracteristica3[1],caracteristica4[0],caracteristica4[1],caracteristica5[0],caracteristica5[1],caracteristica6[0],caracteristica6[1],caracteristica7,caracteristica8,numero,i])
        ruta='prueba/'#la salida de csv
    
    archivo.close()#una vez terminado el archivo se cierra para su visualizacion
    return salida #se retornal la salida

#def escribirArchivosCSV(n,m):#funcion que escribe, ny m son parametros para definir las fulas y columnas a escribir
 #  archivo=open("archivo.csv","a")
  # for filas in range(0, m):
   #print(")