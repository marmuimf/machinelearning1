from PIL import Image #carga libreria img de una carpeta
import os #leer dentro de carpeta
import json

carpeta = "001-crudo"
carpetasalida = "002-procesadas"
imagenes = []

archivos = os.listdir(carpeta) #lista de archivos que hay en la carpeta

for archivo in archivos:
    imagen = os.path.join(carpeta,archivo) #uno carpeta con el archivo
    miimagen = Image.open(imagen)
    anchura = miimagen.width #accedo a la anchura para recortarla (a cuadrada) y reescalarla
    altura = miimagen.height
   
    if anchura > altura:
        caja = ( #caja=tupla
             anchura/2-altura/2,
             0,
             anchura/2+altura/2,
             altura
             )
    else:
        caja = (
             0, # x sera 0
             altura/2-anchura/2,
             anchura,
             altura/2+anchura/2
             )
    
    cortada = miimagen.crop(caja)
    escalada = cortada.resize((512,512)) 
    escalada.save(carpetasalida+"/"+archivo) #guardamos la imagen escalada y recortada, ocupa menos
    imagenes.append(archivo)

#genero json
archivojson = open("json/imagenes.json","w") #abro en modo escritura
json.dump(imagenes,archivojson)#guardo las imagenes
archivojson.close()