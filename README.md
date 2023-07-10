# Cámara Inteligente 
# Semana Tec Herramientas Computacionales

## Integrantes del equipo
Andrea Velázquez de Dios <br/>
Rodrigo López Valencia <br/>
Javier Campos Figueroa <br/>
Gabriel Granda Hervas <br/>
Lucas Wong Mang <br/>

## Instalar dependencias necesarias

Después de clonar este repositorio, es necesario instalar:
- Python3
- OpenCV
- Matplotlib

## Aplicaciones

El archivo main.py está compuesto por un condicional que, dependiendo de la entrada del usuario, correrá el filtro indicado, dichos filtros se pueden correr por separado en los siguientes archivos y a continuación se explican brevemente:

- filtro1.py: Este filtro abre la cámara y no coloca ningún filtro. 
- Filtro2.py: Este filtro invierte los colores de la imagen.
- filtro3.py: Este filtro difumina la imagen.
- filtro4.py: Este filtro gira 180° la imagen, se podría decir que te pone de cabeza.
- filtro5.py: Este filtro hace que solo se vea en la imagen cualquier pixel de "tono de piel" y los demás en negro.
- filtro6.py: Este filtro convierte la imagen a escala de grises.
- filtro7.py: Este filtro hace un efecto de acuarela a la imagen.
- Filtro8.py: Este filtro nos da una imagen como visión térmica

## Ejecución del código

Para poder ejectutar los codigos se deben imoprtar las siguientes librerías.
- cv2: esta librería es clave ya que fue diseñada para "computer vision".
- time: utilizada para mostrar al usuario por cuánto tiempo fue corrido el código.
- argparse: que facilita la escritura de interfaces de línea de comandos, en este código nos ayuda a abrir la cámara.
- numpy: en ciertos filtros se utilizan arreglos de numpy para facilitar el manejo de los pixeles.
- matplotlib: utilizada en el filtro 8 por su paleta de colores cálidos.

## Referencias de código

- "How to Apply Image Filters in OpenCV with Python." (2018). OpenCV and Python Tutorial #8.  [Video]. YouTube. Recuperado de https://www.youtube.com/watch?v=MVLuexuikv4.
- "Smoothing Images." (2021). Image Processing in OpenCV. OpenCV.org. Recuperado de https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html.
- "Changing Colorspaces." (2021) Image Processing in OpenCV. OpenCV.org. Recuperado de https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html.
-  "Python OpenCV painting realizes oil painting effect and watercolor effect." ProgrammersOught. (2021). Recuperado de https://www.programmersought.com/article/57656954509/
-  Donnerstag, B. "Creating fake thermal images using Python".(2017). Bastelhalde. Recuperado de https://bastelhalde.de/post/creating-fake-thermal-images-using-python.
