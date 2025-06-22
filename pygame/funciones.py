import time
import pygame
import sys
import pygame.mixer as mixer 
import random
import os

def musica_ambiental (condicion):

    if condicion:
        mixer.music.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/musica_ambiental.mp3')
        mixer.music.set_volume(0.4)
        mixer.music.play(-1)  
        mixer.music.play()

def efecto_boton (condicion):
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)
    efecto_button.play()

def mostrar_menu ():
    

    # Inicialización
    pygame.init()
    mixer.init()

    """
    mixer.music.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/musica_ambiental.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)  
    """
    """
    #Efecto boton. 
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)
    """

    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_nivel_png.png')
    button_nivel = pygame.transform.scale(button_nivel, (200, 70))
    button_nivel_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_nivel_png_presionado.png')
    button_nivel_presionado = pygame.transform.scale(button_nivel_presionado, (200, 70))

    button_jugar = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_jugar_png.png')
    button_jugar = pygame.transform.scale(button_jugar, (200, 70))
    button_jugar_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_jugar_png_presionado.png')
    button_jugar_presionado = pygame.transform.scale(button_jugar_presionado, (200, 70))

    button_ver_puntaje = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_ver_puntajes_png.png')
    button_ver_puntaje = pygame.transform.scale(button_ver_puntaje, (200, 70))
    button_ver_puntaje_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_ver_puntajes_png_presionado.png')
    button_ver_puntaje_presionado = pygame.transform.scale(button_ver_puntaje_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))

    button_musica_on = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_musica_on_png.png')
    button_musica_on = pygame.transform.scale(button_musica_on, (70, 70))
    button_musica_on_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_musica_on_png_presionado.png')
    button_musica_on_presionado = pygame.transform.scale(button_musica_on_presionado, (70, 70))
    

    button_musica_off = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_musica_off_png.png')
    button_musica_off = pygame.transform.scale(button_musica_off, (70, 70))
    button_musica_off_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_musica_off_png_presionado.png')
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

   

    condicion_musica = True

    musica_ambiental(condicion_musica)

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

        #Boton nivel
        if rectangulo_vertical.collidepoint(pos_mouse):
            imagen_agrandada = pygame.transform.scale(button_nivel_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical_presionado.collidepoint(evento.pos):
              
                    efecto_boton(condicion_musica)
                    time.sleep(0.5)
                    mostrar_niveles(condicion_musica)

        else:  
            PANTALLA.blit(button_nivel, rectangulo_vertical)
                
        #Boton jugar
        if rectangulo_vertical2.collidepoint(pos_mouse):
            imagen_agrandada_2 = pygame.transform.scale(button_jugar_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical2_presionado.collidepoint(evento.pos):

                    efecto_boton(condicion_musica)
                    time.sleep(0.5)
                    numero = random.randint(1,3)
                    generar_nivel(int(numero),condicion_musica)
                    
                    
        else:  
            PANTALLA.blit(button_jugar, rectangulo_vertical2)

        #Boton puntaje
        if rectangulo_vertical3.collidepoint(pos_mouse):
            imagen_agrandada_3 = pygame.transform.scale(button_ver_puntaje_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical3_presionado.collidepoint(evento.pos):

                    efecto_boton(condicion_musica)
                    time.sleep(0.5)
                    mostrar_puntajes(condicion_musica)
        else:  
            PANTALLA.blit(button_ver_puntaje, rectangulo_vertical3)
        
        #Boton salir
        if rectangulo_vertical4.collidepoint(pos_mouse):
            imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical4_presionado.collidepoint(evento.pos):
  
                    efecto_boton(condicion_musica)
                    time.sleep(0.5)
                    pygame.quit()
                    sys.exit()
        else:  
            PANTALLA.blit(button_salir, rectangulo_vertical4)
        
        #Boton sonido
        if condicion_musica:

            if rectangulo_vertical5.collidepoint(pos_mouse):
                imagen_agrandada_5 = pygame.transform.scale(button_musica_on_presionado, (90, 90))  # +20px
                PANTALLA.blit(imagen_agrandada_5, (rectangulo_vertical5_presionado.x - 10, rectangulo_vertical5_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
                    
                    if rectangulo_vertical5_presionado.collidepoint(evento.pos) :
                    
                        condicion_musica = True
                        efecto_boton(condicion_musica)
                        musica_ambiental(condicion_musica)   
                        time.sleep(0.5)  
            else:  
                
                PANTALLA.blit(button_musica_off, rectangulo_vertical6) 

        else:

            if rectangulo_vertical6.collidepoint(pos_mouse):
                imagen_agrandada_6 = pygame.transform.scale(button_musica_off_presionado, (90, 90))  # +20px
                PANTALLA.blit(imagen_agrandada_6, (rectangulo_vertical6_presionado.x - 10, rectangulo_vertical6_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical6_presionado.collidepoint(evento.pos):
                        
                        mixer.music.stop() 
                        condicion_musica = False
                        time.sleep(0.5)        
            else:  
                PANTALLA.blit(button_musica_on, rectangulo_vertical5)


        pygame.display.flip()   


def mostrar_niveles(condicion_musica:bool):
    
    # Inicialización
    pygame.init()
    mixer.init()

    
    """
    #Efecto boton.
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)
    """


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel_facil = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_facil_png.png')
    button_nivel_facil = pygame.transform.scale(button_nivel_facil, (200, 70))
    button_nivel_facil_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_facil_png_presionado.png')
    button_nivel_facil_presionado = pygame.transform.scale(button_nivel_facil_presionado, (200, 70))

    button_nivel_medio = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_medio_png.png')
    button_nivel_medio = pygame.transform.scale(button_nivel_medio, (200, 70))
    button_nivel_medio_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_medio_png_presionado.png')
    button_nivel_medio_presionado = pygame.transform.scale(button_nivel_medio_presionado, (200, 70))

    button_nivel_dificil = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_dificil_png.png')
    button_nivel_dificil = pygame.transform.scale(button_nivel_dificil, (200, 70))
    button_nivel_dificil_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_dificil_png_presionado.png')
    button_nivel_dificil_presionado = pygame.transform.scale(button_nivel_dificil_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
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
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(1)
                            

            else:  
                PANTALLA.blit(button_nivel_facil, rectangulo_vertical)
                    
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_2 = pygame.transform.scale(button_nivel_medio_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(2)
                            
            else:  
                PANTALLA.blit(button_nivel_medio, rectangulo_vertical2)

            if rectangulo_vertical3.collidepoint(pos_mouse):
                imagen_agrandada_3 = pygame.transform.scale(button_nivel_dificil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(3)
                            
            else:  
                PANTALLA.blit(button_nivel_dificil, rectangulo_vertical3)
            
            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        mostrar_menu()
                        
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)



            pygame.display.flip()   


def mostrar_puntajes (condicion_musica:bool):
    # Inicialización
    pygame.init()
    mixer.init()

  
    """
    #Efecto boton.
    efecto_button = mixer.Sound('C:/Users/Matias/Desktop/recursos_musica/ruido_boton.mp3')
    efecto_button.set_volume(0.4)
    """

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
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical2)




            pygame.display.flip()  





def generar_nivel(tipo_nivel: int, condicion_musica:bool):
    # Inicialización
    pygame.init()
    mixer.init()

    mixer.music.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/musica_jugando.mp3')
    mixer.music.set_volume(0.4)  # Empieza en silencio
    mixer.music.play(-1)  # Reproduce en bucle con un fade-in de 1 segundo
    if condicion_musica:   
        mixer.music.play()

    efecto_agua_fallo = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_agua_fallo.mp3')
    efecto_agua_fallo.set_volume(0.4)

    efecto_golpe_barco = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_golpe_barco.mp3')
    efecto_golpe_barco.set_volume(0.4)

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))

    button_reiniciar = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_reiniciar_png.png')
    button_reiniciar = pygame.transform.scale(button_reiniciar, (200, 70))
    button_reiniciar_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_reiniciar_png_presionado.png')
    button_reiniciar_presionado = pygame.transform.scale(button_reiniciar_presionado, (200, 70))

    rectangulo_vertical4 = button_salir.get_rect(x=430, y=680)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=430, y=680)

    rectangulo_vertical = button_reiniciar.get_rect(x=170, y=680)
    rectangulo_vertical_presionado = button_reiniciar_presionado.get_rect(x=170, y=680)



    # Obtener ruta base del proyecto (independiente del usuario)
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Cargar recursos con rutas relativas
    try:

        
        # Imagen de fondo
        fondo_path = os.path.join(base_path, 'recursos_png', 'fondo_menu_png.png')
        imagen_fondo = pygame.image.load(fondo_path)
        imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 800))
    except Exception as e:
        print(f"Error cargando recursos: {e}")
        pygame.quit()
        sys.exit()

    # Configuración de pantalla
    ANCHO, ALTO = 800, 800
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(f"Batalla Naval - Nivel {tipo_nivel}")
    FPS = 25
    clock = pygame.time.Clock()

    # Determinar tamaño del tablero según nivel
    if tipo_nivel == 1:
        filas, columnas = 10, 10
    elif tipo_nivel == 2:
        filas, columnas = 20, 20
    else:  # tipo_nivel == 3
        filas, columnas = 40, 40  # Reducido de 40x40 para mejor visualización

    # Crear y poblar matriz
    matriz = iniciar_matriz(filas, columnas, 0)
    matriz, posiciones_barcos = colocar_barcos(matriz, tipo_nivel)

    matriz_jugador = iniciar_matriz(filas, columnas, 0)


    coordenadas_barcos = []
    coordenadas_y_recoridas = []

    for i in range(filas):
        for x in range(columnas):
            if matriz[i][x] == 1:
                coordenadas_barcos.append((i,x))
                
                

    margen = 2
    ancho_casilla = min(
        (500 - (columnas + 1) * margen) // columnas,
        (500 - (filas + 1) * margen) // filas
    )
    
    # Calcular offsets para centrado
    tablero_ancho = columnas * (ancho_casilla + margen) + margen
    tablero_alto = filas * (ancho_casilla + margen) + margen
    offset_x = (800 - tablero_ancho) // 2  # 800 es ANCHO de tu pantalla
    offset_y = (800 - tablero_alto) // 2   # 800 es ALTO de tu pantalla

    
    condicion = True

    # Bucle principal del juego
    running = True
    while running:
        clock.tick(FPS)
        
        
        for evento in pygame.event.get():
            
           

            

            pos_mouse = pygame.mouse.get_pos()
        
            celda = obtener_celda_click(
                pos_mouse[0], 
                pos_mouse[1],
                filas=filas,
                columnas=columnas,
                ancho_casilla=ancho_casilla,
                margen=margen,
                offset_x=offset_x,
                offset_y=offset_y
            )

            if celda:
                fila, columna = celda
                print(f"Click en fila {fila}, columna {columna}")
                # Aquí tu lógica para manejar el click
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    print("presiona")
                    
                    
                    if (fila,columna) in coordenadas_y_recoridas:
                         condicion = False

                    if condicion:
                        if (fila,columna) in coordenadas_barcos:
                            matriz_jugador[fila][columna] = matriz_jugador[fila][columna] + 1
                            print("Barco hundido")

                            verificar_barcos_hundidos(matriz_jugador, coordenadas_barcos)  

                            coordenadas_y_recoridas.append((fila,columna))

                             
                            
                        if condicion_musica:
                            efecto_golpe_barco.play()
                            
                            
                        
                        else:
                            matriz_jugador[fila][columna] = 2 
                            if condicion_musica:
                                efecto_agua_fallo.play()
                            

                    condicion = True
                            
                           



            # Dibujar
            PANTALLA.blit(imagen_fondo, (0, 0))
            dibujar_tablero(matriz_jugador, filas, columnas, 500, 500, PANTALLA)

            

            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)

            
            if rectangulo_vertical.collidepoint(pos_mouse):
                imagen_agrandada = pygame.transform.scale(button_reiniciar_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        
                        generar_nivel(tipo_nivel, condicion_musica)
            else:  
                PANTALLA.blit(button_reiniciar, rectangulo_vertical)



            pygame.display.flip()

def verificar_barcos_hundidos(matriz_jugador, coordenadas_barcos):
    """
    Verifica si todos los barcos han sido hundidos y si finalizar el juego.
    Args:
        matriz_jugador: Matriz del jugador con los disparos realizados.
        matriz_barcos: Matriz original con la ubicación de los barcos.
    Returns:
        True si todos los barcos están hundidos, False en caso contrario.
    """
    for fila in range(len(matriz_barcos)):
        for col in range(len(matriz_barcos[0])):
            if matriz_barcos[fila][col] == 1 and matriz_jugador[fila][col] != 1:
                return False
    return True 

def verificar_hundido_nombres(matriz_disparos, barcos_info):
    """
    barcos_info = {
        'destructor1': {'posiciones': [(1,2), (1,3)], 'hundido': False},
        'submarino1': {'posiciones': [(2,5)], 'hundido': False}
    }
    """
    hundidos = []
    
    for nombre, info in barcos_info.items():
        if not info['hundido']:
            if all(matriz_disparos[f][c] == 1 for f, c in info['posiciones']):
                info['hundido'] = True
                hundidos.append(nombre)
    
    return hundidos

def obtener_celda_click(x, y, filas, columnas, ancho_casilla, margen, offset_x, offset_y):
    """
    Versión corregida que considera el tablero centrado
    Args:
        x, y: Coordenadas del mouse (píxeles)
        filas, columnas: Tamaño del tablero
        ancho_casilla: Ancho de cada celda en píxeles
        margen: Espacio entre celdas
        offset_x, offset_y: Desplazamiento del tablero desde los bordes
    Returns:
        Tuple (fila, columna) o None si click fuera del tablero
    """
    # Ajustar coordenadas restando el offset
    x_rel = x - offset_x
    y_rel = y - offset_y
    
    # Si el click está fuera del área del tablero
    if x_rel < 0 or y_rel < 0:
        return None
    
    # Calcular posición relativa considerando márgenes
    col = x_rel // (ancho_casilla + margen)
    fila = y_rel // (ancho_casilla + margen)
    
    # Verificar límites del tablero
    if 0 <= fila < filas and 0 <= col < columnas:
        return (fila, col)
    return None



def dibujar_tablero(matriz, filas, columnas, area_ancho, area_alto, pantalla):
    """Dibuja el tablero con imágenes en lugar de colores"""
    # Cargar las imágenes (hazlo una vez al inicio del juego)
    agua_img = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/agua_nivel_png.png')
    barco_img = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/barco_golpeado_png.png')
    fallo_img = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/agua_nivel_fallo_png.png')
    
    # Escalar las imágenes al tamaño de las celdas
    margen = 2
    ancho_casilla = min(
        (area_ancho - (columnas + 1) * margen) // columnas,
        (area_alto - (filas + 1) * margen) // filas
    )
    
    # Escalar imágenes al tamaño de la celda
    agua_img = pygame.transform.scale(agua_img, (ancho_casilla, ancho_casilla))
    barco_img = pygame.transform.scale(barco_img, (ancho_casilla, ancho_casilla))
    fallo_img = pygame.transform.scale(fallo_img, (ancho_casilla, ancho_casilla))

    # Calcular posición del tablero
    tablero_ancho = columnas * (ancho_casilla + margen) + margen
    tablero_alto = filas * (ancho_casilla + margen) + margen
    offset_x = (pantalla.get_width() - tablero_ancho) // 2
    offset_y = (pantalla.get_height() - tablero_alto) // 2

    for fila in range(filas):
        for col in range(columnas):
            x = offset_x + (margen + ancho_casilla) * col + margen
            y = offset_y + (margen + ancho_casilla) * fila + margen
            
            # Seleccionar imagen según el estado de la celda
            if matriz[fila][col] == 0:  # Agua
                pantalla.blit(agua_img, (x, y))
            elif matriz[fila][col] == 1:  # Fallo
                pantalla.blit(barco_img, (x, y))
            else:  # Barco
                pantalla.blit(fallo_img, (x, y))
            
            # Opcional: mantener el borde negro
            rect = pygame.Rect(x, y, ancho_casilla, ancho_casilla)
            pygame.draw.rect(pantalla, (0, 0, 0), rect, 1)

        






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


"""
def colocar_barcos(matriz, dificultad):
    
    Coloca barcos en la matriz según la dificultad:
    1 = Fácil (cantidad normal)
    2 = Medio (doble cantidad)
    3 = Difícil (triple cantidad)
    Los barcos no se tocarán entre sí (incluyendo diagonales)
    
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

"""

def colocar_barcos(matriz, dificultad):
    """
    Coloca barcos en la matriz según la dificultad y retorna:
    - matriz con barcos colocados
    - diccionario con posiciones de cada barco
    
    Estructura del diccionario:
    {
        'submarino': [(f1,c1), (f2,c2), ...],
        'destructor': [(f3,c3), (f4,c4), ...],
        ...
    }
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
    
    # Diccionario para guardar posiciones
    posiciones_barcos = {barco['nombre']: [] for barco in barcos_base}
    
    # Lista de tamaños de barcos a colocar
    barcos_a_colocar = []
    for barco in barcos_base:
        barcos_a_colocar.extend([(barco['nombre'], barco['tamaño'])] * (barco['cantidad'] * multiplicador))
    
    # Ordenar de mayor a menor para mejor colocación
    barcos_a_colocar.sort(key=lambda x: x[1], reverse=True)
    
    for nombre, tamaño in barcos_a_colocar:
        colocado = False
        intentos = 0
        posiciones_barco_actual = []
        
        while not colocado and intentos < 100:
            intentos += 1
            horizontal = random.choice([True, False])
            posiciones_barco_actual = []
            
            if horizontal:
                fila = random.randint(0, filas - 1)
                col_inicio = random.randint(0, columnas - tamaño)
                col_fin = col_inicio + tamaño
                
                # Verificar área alrededor del barco
                espacio_libre = True
                for col in range(max(0, col_inicio-1), min(columnas, col_fin+1)):
                    for f in range(max(0, fila-1), min(filas, fila+2)):
                        if matriz[f][col] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Guardar posiciones y colocar barco
                    for col in range(col_inicio, col_fin):
                        matriz[fila][col] = 1
                        posiciones_barco_actual.append((fila, col))
                    colocado = True
            else:
                col = random.randint(0, columnas - 1)
                fila_inicio = random.randint(0, filas - tamaño)
                fila_fin = fila_inicio + tamaño
                
                # Verificar área alrededor del barco
                espacio_libre = True
                for fila in range(max(0, fila_inicio-1), min(filas, fila_fin+1)):
                    for c in range(max(0, col-1), min(columnas, col+2)):
                        if matriz[fila][c] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Guardar posiciones y colocar barco
                    for fila in range(fila_inicio, fila_fin):
                        matriz[fila][col] = 1
                        posiciones_barco_actual.append((fila, col))
                    colocado = True
        
            if colocado:
                posiciones_barcos[nombre].append(posiciones_barco_actual)
    
    return matriz, posiciones_barcos


    

