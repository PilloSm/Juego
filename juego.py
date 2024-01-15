import pygame,os
from bd import ConexionBD
conexion=ConexionBD()
pygame.init()
dt = 0
tra=False
size = (1000, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego tilin")
clock = pygame.time.Clock()
running = True
black = (255, 255, 255)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class pelota:
    def __init__(self):
        self.image_vida = pelota = pygame.image.load(os.path.join(os.path.dirname(__file__), "Image", "barra.png"))
        self.rect = self.image_vida.get_rect()
        self.rect.move_ip(500, 10)


def Juego():
    pygame.mouse.set_visible(False)
    global player_pos, tra, screen
    hasperdido = pygame.image.load(os.path.join(os.path.dirname(__file__), "Image", "Hasganado.png")).convert()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    running = False                    
        screen.fill("black")
        pygame.draw.circle(screen, black, player_pos, 20)
        pygame.draw.rect(screen, black, (200, 400, 20, 20))
        keys = pygame.key.get_pressed()
        mult = 1
        if keys[pygame.K_LSHIFT]:
            mult = 2
        if keys[pygame.K_w]:
            if player_pos.y > 20:
                player_pos.y -= 200 * dt * mult
        if keys[pygame.K_s]:
            if player_pos.y < size[1] - 20:
                player_pos.y += 200 * dt * mult
        if keys[pygame.K_a]:
            if player_pos.x > 20:
                player_pos.x -= 200 * dt * mult
        if keys[pygame.K_d]:
            if player_pos.x < size[0] - 20:
                player_pos.x += 200 * dt * mult
        pygame.display.flip()
        dt = clock.tick(60) / 1000


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
        pygame.mouse.set_visible(False)
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
                    elif botones[2]["selected"]:
                        conexion.ejecutar_query(f"INSERT INTO juego_principal SET posicion='{player_pos}'")
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
    conexion.inicializar_base_datos()     
    carro=Juego()
    if carro!=False:
            menu()

main()