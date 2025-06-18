import time
import pygame
import sys
import pygame.mixer as mixer 
import random




def mostrar_menu ():
    

    # Inicialización
    pygame.init()
    mixer.init()

    # Música
    mixer.music.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_musica/musica_ambiental.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)  

    #Efecto boton. 
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_nivel_png.png')
    button_nivel = pygame.transform.scale(button_nivel, (200, 70))
    button_nivel_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_nivel_png_presionado.png')
    button_nivel_presionado = pygame.transform.scale(button_nivel_presionado, (200, 70))

    button_jugar = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_jugar_png.png')
    button_jugar = pygame.transform.scale(button_jugar, (200, 70))
    button_jugar_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_jugar_png_presionado.png')
    button_jugar_presionado = pygame.transform.scale(button_jugar_presionado, (200, 70))

    button_ver_puntaje = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_ver_puntajes_png.png')
    button_ver_puntaje = pygame.transform.scale(button_ver_puntaje, (200, 70))
    button_ver_puntaje_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_ver_puntajes_png_presionado.png')
    button_ver_puntaje_presionado = pygame.transform.scale(button_ver_puntaje_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))

    button_musica_on = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_musica_on_png.png')
    button_musica_on = pygame.transform.scale(button_musica_on, (70, 70))
    button_musica_on_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_musica_on_png_presionado.png')
    button_musica_on_presionado = pygame.transform.scale(button_musica_on_presionado, (70, 70))
    

    button_musica_off = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_musica_off_png.png')
    button_musica_off = pygame.transform.scale(button_musica_off, (70, 70))
    button_musica_off_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_musica_off_png_presionado.png')
    button_musica_off_presionado = pygame.transform.scale(button_musica_off_presionado, (70, 70))

    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    FPS = 20
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = button_nivel.get_rect(x=300, y=120)
    rectangulo_vertical_presionado = button_nivel_presionado.get_rect(x=300, y=120)

    rectangulo_vertical2 = button_jugar.get_rect(x=300, y=220)
    rectangulo_vertical2_presionado = button_jugar_presionado.get_rect(x=300, y=220)

    rectangulo_vertical3 = button_ver_puntaje.get_rect(x=300, y=320)
    rectangulo_vertical3_presionado = button_ver_puntaje_presionado.get_rect(x=300, y=320)

    rectangulo_vertical4 = button_salir.get_rect(x=300, y=420)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=300, y=420)

    rectangulo_vertical5 = button_musica_on.get_rect(x=700, y=20)
    rectangulo_vertical5_presionado = button_musica_on_presionado.get_rect(x=700, y=20)

    rectangulo_vertical6 = button_musica_off.get_rect(x=700, y=20)
    rectangulo_vertical6_presionado = button_musica_off_presionado.get_rect(x=700, y=20)

    efecto_activado = True

    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    rectangulo_vertical.y += 100
                if evento.key == pygame.K_UP:
                    rectangulo_vertical.y += -100
                if evento.key == pygame .K_RIGHT:
                    rectangulo_vertical.x += 100
                if evento.key == pygame .K_LEFT:
                    rectangulo_vertical.x += -100


        PANTALLA.blit(imagen_fondo, (0, 0))

        
        

        pos_mouse = pygame.mouse.get_pos()  # Devuelve (x, y)
            # Verificar colisión con un rectángulo (botón, imagen, etc.)
        if rectangulo_vertical.collidepoint(pos_mouse):
            imagen_agrandada = pygame.transform.scale(button_nivel_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical_presionado.collidepoint(evento.pos):
                    if efecto_activado:
                        efecto_button.play()
                    time.sleep(0.5)
                    mostrar_niveles(efecto_activado)

        else:  
            PANTALLA.blit(button_nivel, rectangulo_vertical)
                
        if rectangulo_vertical2.collidepoint(pos_mouse):
            imagen_agrandada_2 = pygame.transform.scale(button_jugar_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                    if efecto_activado:
                        efecto_button.play()
                    time.sleep(0.5)
                    numero = random.randint(1, 3)
                    generar_nivel(int(numero))
                    
                    
        else:  
            PANTALLA.blit(button_jugar, rectangulo_vertical2)

        if rectangulo_vertical3.collidepoint(pos_mouse):
            imagen_agrandada_3 = pygame.transform.scale(button_ver_puntaje_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                    if efecto_activado:
                        efecto_button.play()
                    time.sleep(0.5)
                    mostrar_puntajes(efecto_activado)
        else:  
            PANTALLA.blit(button_ver_puntaje, rectangulo_vertical3)
        
        if rectangulo_vertical4.collidepoint(pos_mouse):
            imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                    if efecto_activado:
                        efecto_button.play()
                    time.sleep(0.5)
                    pygame.quit()
                    sys.exit()
        else:  
            PANTALLA.blit(button_salir, rectangulo_vertical4)
        

        if efecto_activado:

            if rectangulo_vertical5.collidepoint(pos_mouse):
                imagen_agrandada_5 = pygame.transform.scale(button_musica_on_presionado, (90, 90))  # +20px
                PANTALLA.blit(imagen_agrandada_5, (rectangulo_vertical5_presionado.x - 10, rectangulo_vertical5_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
                    
                    if rectangulo_vertical5_presionado.collidepoint(evento.pos) :
                        efecto_activado = False
                        efecto_button.play()
                        mixer.music.play()    
                        time.sleep(0.5)  
            else:  
                
                PANTALLA.blit(button_musica_off, rectangulo_vertical6) 

        else:

            if rectangulo_vertical6.collidepoint(pos_mouse):
                imagen_agrandada_6 = pygame.transform.scale(button_musica_off_presionado, (90, 90))  # +20px
                PANTALLA.blit(imagen_agrandada_6, (rectangulo_vertical6_presionado.x - 10, rectangulo_vertical6_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical6_presionado.collidepoint(evento.pos):
                        efecto_activado = True
                        mixer.music.stop() 
                        time.sleep(0.5)        
            else:  
                PANTALLA.blit(button_musica_on, rectangulo_vertical5)


        pygame.display.flip()   


def mostrar_niveles(efecto_activado:bool):
    
    # Inicialización
    pygame.init()
    mixer.init()

  

    #Efecto boton.
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel_facil = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_facil_png.png')
    button_nivel_facil = pygame.transform.scale(button_nivel_facil, (200, 70))
    button_nivel_facil_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_facil_png_presionado.png')
    button_nivel_facil_presionado = pygame.transform.scale(button_nivel_facil_presionado, (200, 70))

    button_nivel_medio = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_medio_png.png')
    button_nivel_medio = pygame.transform.scale(button_nivel_medio, (200, 70))
    button_nivel_medio_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_medio_png_presionado.png')
    button_nivel_medio_presionado = pygame.transform.scale(button_nivel_medio_presionado, (200, 70))

    button_nivel_dificil = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_dificil_png.png')
    button_nivel_dificil = pygame.transform.scale(button_nivel_dificil, (200, 70))
    button_nivel_dificil_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_dificil_png_presionado.png')
    button_nivel_dificil_presionado = pygame.transform.scale(button_nivel_dificil_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    FPS = 25
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = button_nivel_facil.get_rect(x=80, y=220)
    rectangulo_vertical_presionado = button_nivel_facil_presionado.get_rect(x=80, y=220)

    rectangulo_vertical2 = button_nivel_medio.get_rect(x=300, y=220)
    rectangulo_vertical2_presionado = button_nivel_medio_presionado.get_rect(x=300, y=220)

    rectangulo_vertical3 = button_nivel_dificil.get_rect(x=520, y=220)
    rectangulo_vertical3_presionado = button_nivel_dificil_presionado.get_rect(x=520, y=220)

    rectangulo_vertical4 = button_salir.get_rect(x=300, y=400)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=300, y=400)



    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():

            


            PANTALLA.blit(imagen_fondo, (0, 0))

        
        

            pos_mouse = pygame.mouse.get_pos()  # Devuelve (x, y)
                # Verificar colisión con un rectángulo (botón, imagen, etc.)
            if rectangulo_vertical.collidepoint(pos_mouse):
                imagen_agrandada = pygame.transform.scale(button_nivel_facil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical_presionado.collidepoint(evento.pos):
                        if efecto_activado:
                            efecto_button.play()
                        time.sleep(0.5)
                            

            else:  
                PANTALLA.blit(button_nivel_facil, rectangulo_vertical)
                    
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_2 = pygame.transform.scale(button_nivel_medio_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        if efecto_activado:
                            efecto_button.play()
                        time.sleep(0.5)
                            
            else:  
                PANTALLA.blit(button_nivel_medio, rectangulo_vertical2)

            if rectangulo_vertical3.collidepoint(pos_mouse):
                imagen_agrandada_3 = pygame.transform.scale(button_nivel_dificil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                        if efecto_activado:
                            efecto_button.play()
                        time.sleep(0.5)
                            
            else:  
                PANTALLA.blit(button_nivel_dificil, rectangulo_vertical3)
            
            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        if efecto_activado:
                            efecto_button.play()
                        time.sleep(0.5)
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)



            pygame.display.flip()   


def mostrar_puntajes (efecto_activado:bool):
    # Inicialización
    pygame.init()
    mixer.init()

  

    #Efecto boton.
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    lista_puntaje = pygame.image.load('C:/Users/Matias/Desktop/recursos_png/lista_ver_puntaje_png.png')
    lista_puntaje = pygame.transform.scale(lista_puntaje, (500, 400))
 

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    FPS = 25
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = lista_puntaje.get_rect(x=150, y=50)
    
    rectangulo_vertical2 = button_salir.get_rect(x=300, y=460)
    rectangulo_vertical2_presionado = button_salir_presionado.get_rect(x=300, y=460)



    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():

            


            PANTALLA.blit(imagen_fondo, (0, 0))
            PANTALLA.blit(lista_puntaje, rectangulo_vertical)

        
        

            pos_mouse = pygame.mouse.get_pos()  # Devuelve (x, y)
             
            
                    

            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        if efecto_activado:
                            efecto_button.play()
                        time.sleep(0.5)
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical2)



            pygame.display.flip()  



def generar_nivel(tipo_nivel:int): #matriz_barcos
    # Inicialización
    pygame.init()
    mixer.init()

    #Efecto boton.
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)

    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/utn programacion - copia (1)/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    FPS = 25
    clock = pygame.time.Clock()

    filas = 10
    columnas = 10
    agua = (0,0,255)
    barco_tocado = (0,255,0)
    fallo = (255,0,0)
    margen = 5
    ancho_casilla = 40
    


    if tipo_nivel == 1:
        matriz  = iniciar_matriz(10, 10, 0)
        matriz = colocar_barcos(matriz, tipo_nivel)
    elif tipo_nivel == 2:
        matriz = iniciar_matriz(20, 20, 0)
        matriz = colocar_barcos(matriz, tipo_nivel)
    else:
        matriz = iniciar_matriz(40, 40, 0)
        matriz = colocar_barcos(matriz, tipo_nivel)

    mostrar_matriz(matriz)

    while True:

        PANTALLA.blit(imagen_fondo,(0,0))
        pygame.display.flip()  
    
    





def mostrar_matriz(matriz_barcos):
    # Recorre cada fila de la matriz
    for i in range(len(matriz_barcos)):
        # Recorre cada elemento de la fila actual
        for j in range(len(matriz_barcos[i])):                
            # Imprime el elemento sin salto de línea, dejando un espacio entre elementos
            print(matriz_barcos[i][j], end=" ")
        # Cuando termina la fila, imprime un salto de línea
        print("")




def iniciar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    #esta funcion tiene la tarea de crear una matriz vacía
    #recibe cant_filas, cant_columnas y un valor con el cual rellenar
    #retornará una matriz
    matriz= []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz



def colocar_barcos(matriz, dificultad):
    """
    Coloca barcos en la matriz según la dificultad:
    1 = Fácil (cantidad normal)
    2 = Medio (doble cantidad)
    3 = Difícil (triple cantidad)
    Los barcos no se tocarán entre sí (incluyendo diagonales)
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Definición de barcos
    barcos_base = [
        {'nombre': 'submarino', 'tamaño': 1, 'cantidad': 4},
        {'nombre': 'destructor', 'tamaño': 2, 'cantidad': 3},
        {'nombre': 'crucero', 'tamaño': 3, 'cantidad': 2},
        {'nombre': 'acorazado', 'tamaño': 4, 'cantidad': 1}
    ]
    
    # Ajustar cantidad según dificultad
    multiplicador = 1
    if dificultad == 2:
        multiplicador = 2
    elif dificultad == 3:
        multiplicador = 3
    
    barcos = []
    for barco in barcos_base:
        barcos.extend([barco['tamaño']] * (barco['cantidad'] * multiplicador))
    
    # Ordenar de mayor a menor para mejor colocación
    barcos.sort(reverse=True)
    
    for tamaño in barcos:
        colocado = False
        intentos = 0
        
        while not colocado and intentos < 100:
            intentos += 1
            horizontal = random.choice([True, False])
            
            if horizontal:
                fila = random.randint(0, filas - 1)
                col_inicio = random.randint(0, columnas - tamaño)
                col_fin = col_inicio + tamaño
                
                # Verificar área alrededor del barco (incluyendo 1 casilla de buffer)
                espacio_libre = True
                for col in range(max(0, col_inicio-1), min(columnas, col_fin+1)):
                    for f in range(max(0, fila-1), min(filas, fila+2)):
                        if matriz[f][col] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Colocar barco
                    for col in range(col_inicio, col_fin):
                        matriz[fila][col] = 1
                    colocado = True
            else:
                col = random.randint(0, columnas - 1)
                fila_inicio = random.randint(0, filas - tamaño)
                fila_fin = fila_inicio + tamaño
                
                # Verificar área alrededor del barco (incluyendo 1 casilla de buffer)
                espacio_libre = True
                for fila in range(max(0, fila_inicio-1), min(filas, fila_fin+1)):
                    for c in range(max(0, col-1), min(columnas, col+2)):
                        if matriz[fila][c] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Colocar barco
                    for fila in range(fila_inicio, fila_fin):
                        matriz[fila][col] = 1
                    colocado = True
        
    
    return matriz




def dibujar_tablero(matriz, filas, columnas, agua, barco_tocado, fallo, margen, ancho_casilla, pantalla):
    """Dibuja el tablero en la pantalla"""
    for fila in range(filas):
        for col in range(columnas):
            valor = matriz[fila][col]
            if valor == 0 or valor == 1:  # 0: agua, 1: barco no descubierto
                color = agua
            elif valor == 2:  # Barco tocado
                color = barco_tocado
            elif valor == 3:  # Disparo fallado
                color = fallo
            
            pygame.draw.rect(pantalla, color,
                [(margen + ancho_casilla) * col + margen,
                 (margen + ancho_casilla) * fila + margen,
                 ancho_casilla, ancho_casilla])
























































def obtener_celda_click(x, y, filas, columnas, ancho_casilla, margen):
    """Convierte coordenadas de pantalla a coordenadas de matriz"""
    col = x // (ancho_casilla + margen)
    fila = y // (ancho_casilla + margen)
    if 0 <= fila < filas and 0 <= col < columnas:
        return fila, col
    return None






    


"""
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
            if evento.button == 1:
                print ("hizo click izquiero")
            if evento.button == 3:
                print ("hizo click derecho")
            if rectangulo_vertical.collidepoint(evento.pos):
                print("¡Acertaste!")
            if rectangulo_vertical2.collidepoint(evento.pos):
                print("¡Acertaste!")
            if rectangulo_vertical3.collidepoint(evento.pos):
                print("¡Acertaste!")
            if rectangulo_vertical4.collidepoint(evento.pos):
                print("¡Acertaste!")
            if rectangulo_vertical5.collidepoint(evento.pos):
                print("¡Acertaste!")
            if rectangulo_vertical6.collidepoint(evento.pos):
                print("¡Acertaste!")
        """