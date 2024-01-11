import pygame, sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Configuración de la pantalla
ancho_pantalla = 400
alto_pantalla = 300
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Botón con Pygame")

# Función para crear el botón
def crear_boton(rect, color_normal, color_presionado, texto, font):
    pygame.draw.rect(pantalla, color_normal, rect)
    pantalla.blit(texto, (rect.x + rect.width // 2 - texto.get_width() // 2, rect.y + rect.height // 2 - texto.get_height() // 2))

# Configuración del botón
boton_rect = pygame.Rect(150, 100, 100, 50)
boton_color_normal = AZUL
boton_color_presionado = BLANCO
boton_presionado = False

# Configuración del texto en el botón
font = pygame.font.Font(None, 36)
texto = font.render("Presionar", True, NEGRO)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(evento.pos):
                boton_presionado = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            boton_presionado = False

    # Cambiar el color del botón según si está presionado o no
    if boton_presionado:
        crear_boton(boton_rect, boton_color_presionado, boton_color_presionado, texto, font)
    else:
        crear_boton(boton_rect, boton_color_normal, boton_color_presionado, texto, font)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de actualización
    pygame.time.Clock().tick(30)
