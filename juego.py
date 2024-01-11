import pygame
import os

pygame.init()

size = (1000, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego tilin")
clock = pygame.time.Clock()
running = True
black = (255, 255, 255)
mov_x = 10
mov_y = 10
speed_x = 3
speed_y = 3
veces = 0


class pelota:
    def __init__(self):
        self.image_vida = pelota = pygame.image.load(os.path.join(os.path.dirname(__file__), "Image", "barra.png"))
        self.rect = self.image_vida.get_rect()
        self.rect.move_ip(500, 10)


def Juego():    
    global mov_x, mov_y, veces, speed_x, speed_y
    hasperdido = pygame.image.load(os.path.join(os.path.dirname(__file__), "Image", "Hasganado.png")).convert()
    running = True
    while running:
        zaz = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    if distance_obj<=100:
                        running=False
        screen.fill("black")
        coordenates = pygame.mouse.get_pos()
        distance = ((mov_x - coordenates[0]) ** 2 + (mov_y - coordenates[1]) ** 2) ** 0.5
        pygame.draw.circle(screen, black if distance >= 20 else (255, 0, 0), (mov_x, mov_y), 20)
        
        objeto=pygame.draw.circle(screen,"white", (130,240),100)

        distance_obj=((mov_x-130)**2 + (mov_y-240)**2)**0.5

        if distance <= 20:
            veces += 1
        if veces >= 100:
            screen.blit(hasperdido, (250, 264))
            mov_x = 10
            mov_y = 10
            veces = 0
            pygame.display.flip()
            pygame.time.delay(2000)  # Espera 2 segundos antes de volver a ejecutar el juego
            return
        mov_y += speed_y
        mov_x += speed_x
        if mov_x >= size[0] or mov_x < 0:
            speed_x *= -1
        if mov_y >= size[1] or mov_y < 0:
            speed_y *= -1
        pygame.display.flip()
        clock.tick(60)


def menu():
    running = True
    botones = [
        {"text": "Volver", "id": 1, "selected": True},
        {"text": "Terminar", "id": 2, "selected": False},
        {"text": "Guardar", "id": 3, "selected": False}
    ]

    def dibujar_botones():
        for boton in botones:
            boton_rect = pygame.draw.rect(screen, black if not boton["selected"] else (0, 0, 255),
                                          (420, boton["id"] * 100, 200, 50))
            font = pygame.font.Font(None, 38)
            texto = font.render(boton["text"], True, "black")
            screen.blit(texto, (430, boton["id"] * 100 + 10))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if botones[1]["selected"]:
                        running = False
                        return False
                    elif botones[0]["selected"]:
                        Juego()
                elif event.key == pygame.K_DOWN:
                    id = 0
                    for boton in botones:
                        if boton["selected"]:
                            id = boton["id"]
                            boton["selected"] = False
                    if id == len(botones):
                        botones[0]["selected"] = True
                    else:
                        for boton in botones:
                            if boton["id"] == id + 1:
                                boton["selected"] = True
                                break
                elif event.key == pygame.K_UP:
                    id = 0
                    for boton in botones:
                        if boton["selected"]:
                            id = boton["id"]
                            boton["selected"] = False
                    if id == 1:
                        botones[-1]["selected"] = True
                    else:
                        for boton in botones:
                            if boton["id"] == id - 1:
                                boton["selected"] = True
                                break

        screen.fill("black")
        dibujar_botones()
        pygame.display.flip()
        clock.tick(60)


def main():
        carro=Juego()
        print(carro)
        if carro!=False:
            menu()

main()
