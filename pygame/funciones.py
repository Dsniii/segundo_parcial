import time
import pygame
import sys
import pygame.mixer as mixer 
import random
import os
import json

def musica_ambiental (condicion):

    if condicion:
        mixer.music.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/musica_ambiental.mp3')
        mixer.music.set_volume(0.4)
        mixer.music.play(-1)  
        mixer.music.play()

def efecto_boton (condicion):
    if condicion:
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
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
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
    condicion_efecto = True 
    
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
                    if condicion_efecto:
                        efecto_boton(True)
                    time.sleep(0.5)
                    mostrar_niveles(condicion_efecto)

        else:  
            PANTALLA.blit(button_nivel, rectangulo_vertical)
                
        #Boton jugar
        if rectangulo_vertical2.collidepoint(pos_mouse):
            imagen_agrandada_2 = pygame.transform.scale(button_jugar_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                    if condicion_efecto:
                        efecto_boton(True)
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
                    if condicion_efecto:
                        efecto_boton(True)
                    time.sleep(0.5)
                    mostrar_puntajes(condicion_efecto)
        else:  
            PANTALLA.blit(button_ver_puntaje, rectangulo_vertical3)
        
        #Boton salir
        if rectangulo_vertical4.collidepoint(pos_mouse):
            imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                    if condicion_efecto:
                        efecto_boton(True)
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
                        print ("musica on")
                        condicion_efecto = False 
                        condicion_musica = False
                        efecto_boton(True)
                        musica_ambiental(True)   
                        time.sleep(0.5)  
            else:  
                
                PANTALLA.blit(button_musica_off, rectangulo_vertical6) 

        else:

            if rectangulo_vertical6.collidepoint(pos_mouse):
                imagen_agrandada_6 = pygame.transform.scale(button_musica_off_presionado, (90, 90))  # +20px
                PANTALLA.blit(imagen_agrandada_6, (rectangulo_vertical6_presionado.x - 10, rectangulo_vertical6_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical6_presionado.collidepoint(evento.pos):
                        print ("musica off")
                        mixer.music.stop()
                        condicion_efecto = False 
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
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
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
                        generar_nivel(1, condicion_musica)
                            

            else:  
                PANTALLA.blit(button_nivel_facil, rectangulo_vertical)
                    
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_2 = pygame.transform.scale(button_nivel_medio_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(2, condicion_musica)
                            
            else:  
                PANTALLA.blit(button_nivel_medio, rectangulo_vertical2)

            if rectangulo_vertical3.collidepoint(pos_mouse):
                imagen_agrandada_3 = pygame.transform.scale(button_nivel_dificil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(3, condicion_musica)
                            
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
    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    lista_puntaje = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/lista_ver_puntaje_png.png')
    lista_puntaje = pygame.transform.scale(lista_puntaje, (500, 400))
 

    button_salir = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
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


            with open('C:/Users/Matias/Desktop/segundo_parcial/pygame/archivos_json/puntajes.json', 'r') as archivo_json:
                datos = json.load(archivo_json)

            jugador_1 = str(datos.get('nombre_1')) + " " + str(datos.get('puntaje_1'))
            jugador_2 = str(datos.get('nombre_2')) + " " + str(datos.get('puntaje_2'))
            jugador_3 = str(datos.get('nombre_3')) + " " + str(datos.get('puntaje_3'))
            # Mostrar los puntajes de los jugadores
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_1, 1)
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_2, 2)
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_3, 3)


            pygame.display.flip()  


def mostrar_puntaje_jugadores_top_3(PANTALLA, texto: str, top: int):
    # Carga de imágenes (como ya tienes)
    texto_A = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_A_png.png')
    texto_A = pygame.transform.scale(texto_A, (30, 40))
    texto_B = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_B_png.png')
    texto_B = pygame.transform.scale(texto_B, (30, 40))
    texto_C = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_C_png.png')
    texto_C = pygame.transform.scale(texto_C, (30, 40))
    texto_D = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_D_png.png')
    texto_D = pygame.transform.scale(texto_D, (30, 40))
    texto_E = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_E_png.png')
    texto_E = pygame.transform.scale(texto_E, (30, 40))
    texto_F = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_F_png.png')
    texto_F = pygame.transform.scale(texto_F, (30, 40))
    texto_G = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_G_png.png')
    texto_G = pygame.transform.scale(texto_G, (30, 40))
    texto_H = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_H_png.png')
    texto_H = pygame.transform.scale(texto_H, (30, 40))
    texto_I = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_I_png.png')
    texto_I = pygame.transform.scale(texto_I, (30, 40))
    texto_J = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_J_png.png')
    texto_J = pygame.transform.scale(texto_J, (30, 40))
    texto_K = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_K_png.png')
    texto_K = pygame.transform.scale(texto_K, (30, 40))
    texto_L = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_L_png.png')
    texto_L = pygame.transform.scale(texto_L, (30, 40))
    texto_M = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_M_png.png')
    texto_M = pygame.transform.scale(texto_M, (30, 40))
    texto_N = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_N_png.png')
    texto_N = pygame.transform.scale(texto_N, (30, 40))
    texto_O = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_O_png.png')
    texto_O = pygame.transform.scale(texto_O, (30, 40))
    texto_P = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_P_png.png')
    texto_P = pygame.transform.scale(texto_P, (30, 40))
    texto_Q = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Q_png.png')
    texto_Q = pygame.transform.scale(texto_Q, (30, 40))
    texto_R = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_R_png.png')
    texto_R = pygame.transform.scale(texto_R, (30, 40))
    texto_S = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_S_png.png')
    texto_S = pygame.transform.scale(texto_S, (30, 40))
    texto_T = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_T_png.png')
    texto_T = pygame.transform.scale(texto_T, (30, 40))
    texto_U = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_U_png.png')
    texto_U = pygame.transform.scale(texto_U, (30, 40))
    texto_V = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_V_png.png')
    texto_V = pygame.transform.scale(texto_V, (30, 40))
    texto_W = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_W_png.png')
    texto_W = pygame.transform.scale(texto_W, (30, 40))
    texto_X = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_X_png.png')
    texto_X = pygame.transform.scale(texto_X, (30, 40))
    texto_Y = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Y_png.png')
    texto_Y = pygame.transform.scale(texto_Y, (30, 40))
    texto_Z = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Z_png.png')
    texto_Z = pygame.transform.scale(texto_Z, (30, 40))
    texto_simobolo_menos = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/simbolo_menos_png.png')
    texto_simobolo_menos = pygame.transform.scale(texto_simobolo_menos, (30, 40))
    texto_cero = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_0_png.png')
    texto_cero = pygame.transform.scale(texto_cero, (30, 30))
    texto_uno = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_1_png.png')
    texto_uno = pygame.transform.scale(texto_uno, (30, 30))
    texto_dos = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_2_png.png')
    texto_dos = pygame.transform.scale(texto_dos, (30, 30))
    texto_tres = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_3_png.png')
    texto_tres = pygame.transform.scale(texto_tres, (30, 30))
    texto_cuatro = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_4_png.png')
    texto_cuatro = pygame.transform.scale(texto_cuatro, (30, 30))
    texto_cinco = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_5_png.png')
    texto_cinco = pygame.transform.scale(texto_cinco, (30, 30))
    texto_seis = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_6_png.png')
    texto_seis = pygame.transform.scale(texto_seis, (30, 30))
    texto_siete = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_7_png.png')
    texto_siete = pygame.transform.scale(texto_siete, (30, 30))
    texto_ocho = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_8_png.png')
    texto_ocho = pygame.transform.scale(texto_ocho, (30, 30))
    texto_nueve = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_9_png.png')
    texto_nueve = pygame.transform.scale(texto_nueve, (30, 30))

    # Diccionario para acceso rápido
    letras = {
        'A': texto_A, 'B': texto_B, 'C': texto_C, 'D': texto_D, 'E': texto_E, 'F': texto_F,
        'G': texto_G, 'H': texto_H, 'I': texto_I, 'J': texto_J, 'K': texto_K, 'L': texto_L,
        'M': texto_M, 'N': texto_N, 'O': texto_O, 'P': texto_P, 'Q': texto_Q, 'R': texto_R,
        'S': texto_S, 'T': texto_T, 'U': texto_U, 'V': texto_V, 'W': texto_W, 'X': texto_X,
        'Y': texto_Y, 'Z': texto_Z, '-': texto_simobolo_menos, '0': texto_cero, '1': texto_uno,
        '2': texto_dos, '3': texto_tres, '4': texto_cuatro, '5': texto_cinco, '6': texto_seis,
        '7': texto_siete, '8': texto_ocho, '9': texto_nueve
    }

    # Posición base (centrado horizontal)
    if top == 1:
        pos_x = 400
        pos_y = 120
    elif top == 2:
        pos_x = 400
        pos_y = 220
    elif top == 3:
        pos_x = 400
        pos_y = 320

    str_puntaje = str(texto).upper()  # Asegura mayúsculas
    ancho_letra = 20
    espacio = 5  # Espacio entre caracteres

    ancho_total = len(str_puntaje) * (ancho_letra + espacio)
    pos_x_inicial = pos_x - ancho_total // 2

    for i, digito in enumerate(str_puntaje):
        x = pos_x_inicial + i * (ancho_letra + espacio)
        if digito == ' ':
            continue  # Deja espacio vacío
        imagen = letras.get(digito)
        if imagen:
            # Ajusta la altura para números (más chicos)
            if digito.isdigit():
                PANTALLA.blit(imagen, (x, pos_y + 10))
            else:
                PANTALLA.blit(imagen, (x, pos_y))



def generar_nivel(tipo_nivel: int, condicion_musica:bool):
    # Inicialización
    pygame.init()
    mixer.init()

    
    
    if condicion_musica:   
        mixer.music.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/musica_jugando.mp3')
        mixer.music.set_volume(0.4)  
        mixer.music.play(-1)

    efecto_ganaste = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_de_ganaste.mp3')
    efecto_ganaste.set_volume(0.4)
    
    efecto_agua_fallo = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_agua_fallo.mp3')
    efecto_agua_fallo.set_volume(0.4)

    efecto_golpe_barco = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_golpe_barco.mp3')
    efecto_golpe_barco.set_volume(0.4)

    efecto_golpe_hundido = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_barco_hundido.mp3')
    efecto_golpe_hundido.set_volume(5.0)

    efecto_golpe_hundido_2 = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_señal.mp3')
    efecto_golpe_hundido_2.set_volume(5.0)

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
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
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

    for fila in matriz:
        print(fila)

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

    condicion_hundimiento = False
    condicion = True

    puntaje_jugador = 0

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

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    print("presiona")

                    if (fila, columna) in coordenadas_y_recoridas:
                        condicion = False
                    else:
                        condicion = True

                    if condicion:
                        if (fila, columna) in coordenadas_barcos:
                            matriz_jugador[fila][columna] += 1
                            puntaje_jugador += 5

                            condicion_hundimiento, tamaño_hundido = verificar_hundidos(matriz_jugador, posiciones_barcos)
                            coordenadas_y_recoridas.append((fila, columna))
                            condicion_efecto = True
                        else:
                            condicion_efecto = False

                        if condicion_hundimiento:
                            if condicion_musica:
                                efecto_golpe_hundido_2.play()
                                efecto_golpe_hundido.play()
                            condicion_hundimiento = False
                            puntaje_jugador += (tamaño_hundido * 10)

                            if todos_barcos_hundidos(coordenadas_barcos, matriz_jugador):
                                if condicion_musica:
                                    efecto_ganaste.play()
                                time.sleep(2.0)
                                ingresar_nombre_jugador(PANTALLA, condicion_musica, puntaje_jugador, tipo_nivel)

                        elif condicion_efecto:
                            if condicion_musica:
                                efecto_golpe_barco.play()
                        else:
                            if matriz_jugador[fila][columna] != 2:
                                matriz_jugador[fila][columna] = 2
                                if condicion_musica:
                                    efecto_agua_fallo.play()
                                puntaje_jugador -= 1

                    print("puntaje jugador:", puntaje_jugador)












                            
                           



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


            mostrar_puntaje_pantalla(puntaje_jugador, PANTALLA)

            pygame.display.flip()

def ingresar_nombre_jugador(PANTALLA, condicion_efecto, puntaje_jugador, tipo_nivel):
    

    ANCHO, ALTO = 800, 400
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    FPS = 20
    clock = pygame.time.Clock()
    
    boton_enter = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/boton_enter_png.png')
    boton_enter = pygame.transform.scale(boton_enter, (200, 70))

    boton_enter_presionando = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/boton_enter_presionado_png.png')
    boton_enter_presionando = pygame.transform.scale(boton_enter_presionando, (200, 70))
    
    tabla_texto = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/cuadro_texto_png.png')
    tabla_texto = pygame.transform.scale(tabla_texto, (450, 100))
    
    

    imagen_fondo = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    # Rectángulos para los botones
    rectangulo_vertical = boton_enter.get_rect(x=300, y=270)
    rectangulo_vertical_presionado = boton_enter_presionando.get_rect(x=300, y=270)

    nombre_jugador = ""
    
    while True:
        clock.tick(FPS)
        for evento in pygame.event.get():
            
            if evento.type == pygame.KEYDOWN:
                
                if len(nombre_jugador) <= 3:  # Limitar a 4 caracteres
                    if evento.unicode.isalpha():
                        print(f"Letra presionada: {evento.unicode}")
                        nombre_jugador += evento.unicode.upper()  # Convertir a mayúscula
                    
                if evento.key == pygame.K_BACKSPACE:
                        nombre_jugador = nombre_jugador[:-1]  # Borrar último carácter

                
            
        

        pos_mouse = pygame.mouse.get_pos()  # Devuelve (x, y)
            # Verificar colisión con un rectángulo (botón, imagen, etc.)

        PANTALLA.blit(imagen_fondo, (0, 0))

        PANTALLA.blit(tabla_texto, (170, 150))


        #Boton nivel
        if rectangulo_vertical.collidepoint(pos_mouse):
            imagen_agrandada = pygame.transform.scale(boton_enter_presionando, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical_presionado.collidepoint(evento.pos):
                    if condicion_efecto:
                        efecto_boton(True)
                    time.sleep(0.5)
                    registrar_puntaje(puntaje_jugador, nombre_jugador, tipo_nivel)
                    mostrar_menu()

        else:  
            PANTALLA.blit(boton_enter, rectangulo_vertical)
                

        mostrar_puntaje_pantalla(puntaje_jugador, PANTALLA )
        
        mostrar_texto_pantalla(nombre_jugador, PANTALLA)
        pygame.display.flip()

        pygame.display.flip()
        

   

def registrar_puntaje(puntaje_jugador, nombre_jugador, nivel):

    with open('C:/Users/Matias/Desktop/segundo_parcial/pygame/archivos_json/puntajes.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
    
    if puntaje_jugador >= int(datos["puntaje_1"]):
        # Desplazar todos hacia abajo
        datos["puntaje_3"] = datos["puntaje_2"]
        datos["nombre_3"] = datos["nombre_2"]
        datos["nivel_3"] = datos["nivel_2"]
        
        datos["puntaje_2"] = datos["puntaje_1"]
        datos["nombre_2"] = datos["nombre_1"]
        datos["nivel_2"] = datos["nivel_1"]
        
        # Insertar nuevo 1er lugar
        datos["puntaje_1"] = puntaje_jugador
        datos["nombre_1"] = nombre_jugador
        datos["nivel_1"] = nivel

    elif puntaje_jugador >= int(datos["puntaje_2"]):
        # Desplazar 2do a 3ro
        datos["puntaje_3"] = datos["puntaje_2"]
        datos["nombre_3"] = datos["nombre_2"]
        datos["nivel_3"] = datos["nivel_2"]
        
        # Insertar nuevo 2do lugar
        datos["puntaje_2"] = puntaje_jugador
        datos["nombre_2"] = nombre_jugador
        datos["nivel_2"] = nivel

    elif puntaje_jugador >= int(datos["puntaje_3"]):
        # Insertar nuevo 3er lugar
        datos["puntaje_3"] = puntaje_jugador
        datos["nombre_3"] = nombre_jugador
        datos["nivel_3"] = nivel
        

# Guardar en archivo
    with open('C:/Users/Matias/Desktop/segundo_parcial/pygame/archivos_json/puntajes.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)  # indent=4 para formato legible



def mostrar_texto_pantalla(texto, PANTALLA):

   

    texto_A = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_A_png.png')
    texto_A = pygame.transform.scale(texto_A, (50, 60))
    
    texto_B = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_B_png.png')
    texto_B = pygame.transform.scale(texto_B, (50, 60))

    texto_C = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_C_png.png')
    texto_C = pygame.transform.scale(texto_C, (50, 60))

    texto_D = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_D_png.png')
    texto_D = pygame.transform.scale(texto_D, (50, 60))

    texto_E = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_E_png.png')
    texto_E = pygame.transform.scale(texto_E, (50, 60))

    texto_F = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_F_png.png')
    texto_F = pygame.transform.scale(texto_F, (50, 60))

    texto_G = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_G_png.png')
    texto_G = pygame.transform.scale(texto_G, (50, 60))

    texto_H = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_H_png.png')
    texto_H = pygame.transform.scale(texto_H, (50, 60))

    texto_I = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_I_png.png')
    texto_I = pygame.transform.scale(texto_I, (50, 60))

    texto_J = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_J_png.png')
    texto_J = pygame.transform.scale(texto_J, (50, 60))

    texto_K = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_K_png.png')
    texto_K = pygame.transform.scale(texto_K, (50, 60))

    texto_L = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_L_png.png')
    texto_L = pygame.transform.scale(texto_L, (50, 60))

    texto_M = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_M_png.png')
    texto_M = pygame.transform.scale(texto_M, (50, 60))

    texto_N = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_N_png.png')
    texto_N = pygame.transform.scale(texto_N, (50, 60))

    texto_O = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_O_png.png')
    texto_O = pygame.transform.scale(texto_O, (50, 60))

    texto_P = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_P_png.png')
    texto_P = pygame.transform.scale(texto_P, (50, 60))

    texto_Q = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Q_png.png')
    texto_Q = pygame.transform.scale(texto_Q, (50, 60))

    texto_R = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_R_png.png')
    texto_R = pygame.transform.scale(texto_R, (50, 60))

    texto_S = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_S_png.png')
    texto_S = pygame.transform.scale(texto_S, (50, 60))

    texto_T = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_T_png.png')
    texto_T = pygame.transform.scale(texto_T, (50, 60))

    texto_U = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_U_png.png')
    texto_U = pygame.transform.scale(texto_U, (50, 60))

    texto_V = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_V_png.png')
    texto_V = pygame.transform.scale(texto_V, (50, 60))

    texto_W = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_W_png.png')
    texto_W = pygame.transform.scale(texto_W, (50, 60))

    texto_X = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_X_png.png')
    texto_X = pygame.transform.scale(texto_X, (50, 60))

    texto_Y = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Y_png.png')
    texto_Y = pygame.transform.scale(texto_Y, (50, 60))
    
    texto_Z = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/caracter_Z_png.png')
    texto_Z = pygame.transform.scale(texto_Z, (50, 60))


    # Posición base (como la tenías)
    pos_x = 810
    pos_y = 170
    
    # Convertir el puntaje a string
    str_puntaje = str(texto)
    
    # Calcular el ancho total del puntaje
    ancho_total = len(str_puntaje) * 55  # 75px por dígito (ajusta si es diferente)
    
    
    # Calcular posición X inicial para centrar
    pos_x_inicial = (pos_x - ancho_total) // 2
    
    # Mostrar cada dígito
    for i, digito in enumerate(str_puntaje):
        if digito == 'A':
            PANTALLA.blit(texto_A, (pos_x_inicial + i*50, pos_y))
        elif digito == 'B':
            PANTALLA.blit(texto_B, (pos_x_inicial + i*50, pos_y))
        elif digito == 'C':
            PANTALLA.blit(texto_C, (pos_x_inicial + i*50, pos_y))
        elif digito == 'D':
            PANTALLA.blit(texto_D, (pos_x_inicial + i*50, pos_y))
        elif digito == 'E':
            PANTALLA.blit(texto_E, (pos_x_inicial + i*50, pos_y))
        elif digito == 'F':
            PANTALLA.blit(texto_F, (pos_x_inicial + i*50, pos_y))
        elif digito == 'G':
            PANTALLA.blit(texto_G, (pos_x_inicial + i*50, pos_y))
        elif digito == 'H':
            PANTALLA.blit(texto_H, (pos_x_inicial + i*50, pos_y))
        elif digito == 'I':
            PANTALLA.blit(texto_I, (pos_x_inicial + i*50, pos_y))
        elif digito == 'J':
            PANTALLA.blit(texto_J, (pos_x_inicial + i*50, pos_y))
        elif digito == 'K':
            PANTALLA.blit(texto_K, (pos_x_inicial + i*50, pos_y))
        elif digito == 'L':
            PANTALLA.blit(texto_L, (pos_x_inicial + i*50, pos_y))
        elif digito == 'M':
            PANTALLA.blit(texto_M, (pos_x_inicial + i*50, pos_y))
        elif digito == 'N':
            PANTALLA.blit(texto_N, (pos_x_inicial + i*50, pos_y))
        elif digito == 'O':
            PANTALLA.blit(texto_O, (pos_x_inicial + i*50, pos_y))
        elif digito == 'P':
            PANTALLA.blit(texto_P, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Q':
            PANTALLA.blit(texto_Q, (pos_x_inicial + i*50, pos_y))
        elif digito == 'R':
            PANTALLA.blit(texto_R, (pos_x_inicial + i*50, pos_y))
        elif digito == 'S':
            PANTALLA.blit(texto_S, (pos_x_inicial + i*50, pos_y))
        elif digito == 'T':
            PANTALLA.blit(texto_T, (pos_x_inicial + i*50, pos_y))
        elif digito == 'U':
            PANTALLA.blit(texto_U, (pos_x_inicial + i*50, pos_y))
        elif digito == 'V':
            PANTALLA.blit(texto_V, (pos_x_inicial + i*50, pos_y))
        elif digito == 'W':
            PANTALLA.blit(texto_W, (pos_x_inicial + i*50, pos_y))
        elif digito == 'X':
            PANTALLA.blit(texto_X, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Y':
            PANTALLA.blit(texto_Y, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Z':
            PANTALLA.blit(texto_Z, (pos_x_inicial + i*50, pos_y))
    
    

    


def mostrar_puntaje_pantalla(puntaje_jugador, PANTALLA):
    #
    texto_simobolo_menos = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/simbolo_menos_png.png')
    texto_simobolo_menos = pygame.transform.scale(texto_simobolo_menos, (60, 70))

    texto_cero = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_0_png.png')
    texto_cero = pygame.transform.scale(texto_cero, (70, 70))

    texto_uno = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_1_png.png')
    texto_uno = pygame.transform.scale(texto_uno, (70, 70))

    texto_dos = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_2_png.png')
    texto_dos = pygame.transform.scale(texto_dos, (70, 70))

    texto_tres = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_3_png.png')
    texto_tres = pygame.transform.scale(texto_tres, (70, 70))

    texto_cuatro = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_4_png.png')
    texto_cuatro = pygame.transform.scale(texto_cuatro, (70, 70))

    texto_cinco = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_5_png.png')
    texto_cinco = pygame.transform.scale(texto_cinco, (70, 70))

    texto_seis = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_6_png.png')
    texto_seis = pygame.transform.scale(texto_seis, (70, 70))
    
    texto_siete = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_7_png.png')
    texto_siete = pygame.transform.scale(texto_siete, (70, 70))

    texto_ocho = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_8_png.png')
    texto_ocho = pygame.transform.scale(texto_ocho, (70, 70))
    
    texto_nueve = pygame.image.load('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_png/numero_9_png.png')
    texto_nueve = pygame.transform.scale(texto_nueve, (70, 70))

  

    # Posición base (como la tenías)
    pos_x = 810
    pos_y = 60
    
    # Convertir el puntaje a string
    str_puntaje = str(puntaje_jugador)
    
    # Calcular el ancho total del puntaje
    ancho_total = len(str_puntaje) * 75  # 75px por dígito (ajusta si es diferente)
    if '-' in str_puntaje:
        ancho_total -= 15  # Ajuste para el símbolo negativo que es más angosto
    
    # Calcular posición X inicial para centrar
    pos_x_inicial = (pos_x - ancho_total) // 2
    
    # Mostrar cada dígito
    for i, digito in enumerate(str_puntaje):
        if digito == '-':
            PANTALLA.blit(texto_simobolo_menos, (pos_x_inicial + i*75, pos_y))
        elif digito == '0':
            PANTALLA.blit(texto_cero, (pos_x_inicial + i*75, pos_y))
        elif digito == '1':
            PANTALLA.blit(texto_uno, (pos_x_inicial + i*75, pos_y))
        elif digito == '2':
            PANTALLA.blit(texto_dos, (pos_x_inicial + i*75, pos_y))
        elif digito == '3':
            PANTALLA.blit(texto_tres, (pos_x_inicial + i*75, pos_y))
        elif digito == '4':
            PANTALLA.blit(texto_cuatro, (pos_x_inicial + i*75, pos_y))
        elif digito == '5':
            PANTALLA.blit(texto_cinco, (pos_x_inicial + i*75, pos_y))
        elif digito == '6':
            PANTALLA.blit(texto_seis, (pos_x_inicial + i*75, pos_y))
        elif digito == '7':
            PANTALLA.blit(texto_siete, (pos_x_inicial + i*75, pos_y))
        elif digito == '8':
            PANTALLA.blit(texto_ocho, (pos_x_inicial + i*75, pos_y))
        elif digito == '9':
            PANTALLA.blit(texto_nueve, (pos_x_inicial + i*75, pos_y))
    
    








def todos_barcos_hundidos(coordenadas_barcos, matriz_disparos):
    """
    Versión para lista plana de posiciones
    Ejemplo: [(1,2), (1,3), (2,5), (3,1), (3,2), (3,3)]
    """
    for fila, columna in coordenadas_barcos:
        if matriz_disparos[fila][columna] != 1:
            return False
    return True

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




def colocar_barcos(matriz, dificultad):
    
    
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




def verificar_hundidos(matriz_disparos, posiciones_barcos):
    """
    Verifica si algún barco ha sido completamente hundido
    
    Args:
        matriz_disparos: Matriz con 0 (no disparado), 1 (impacto), 2 (fallo)
        posiciones_barcos: Diccionario de barcos y sus posiciones
                         {'submarino': [[(f1,c1)], [(f2,c2)], ...],
                          'destructor': [[(f3,c3), (f4,c4)], ...]}
    
    Returns:
        tuple: (bool_hundido, tamaño_barco_hundido)
               - bool_hundido: True si se hundió al menos un barco
               - tamaño_barco_hundido: Número de celdas del barco hundido (0 si no hubo hundimiento)
    """
    hundido = False
    tamaño_hundido = 0

    for nombre_barco, lista_barcos in posiciones_barcos.items():
        for barco in list(lista_barcos):
            if all(matriz_disparos[f][c] == 1 for f, c in barco):
                hundido = True
                tamaño_hundido = len(barco)  # Obtenemos el tamaño del barco
                lista_barcos.remove(barco)
                break  # Salimos del bucle al encontrar el primer barco hundido
        if hundido:
            break
    
    return (hundido, tamaño_hundido)

