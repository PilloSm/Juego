import pygame, os, mysql.connector

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="LuMITY_BV1",
)
cursor=conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS juego_piolin")

cursor.execute("use juego_piolin")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS juego_principal (
        intento INT AUTO_INCREMENT PRIMARY KEY,
        tiempo varchar (30) not null
    )
""")

pygame.init()
size = (1000, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego tilin")
clock = pygame.time.Clock()
running = True
black = (255, 255, 255)
fondo = pygame.image.load(os.path.join(os.path.dirname(__file__), "Image", "Hasganado.png")).convert()

botones = [
    {"text": "hola", "id": 1, "selected": True},
    {"text": "Terminar", "id": 2, "selected": False},
    {"text": "guardar", "id": 3, "selected": False}
]

def dibujar_botones():
    for boton in botones:
        boton_rect = pygame.draw.rect(screen, black if boton["selected"]==False else "blue", (420, boton["id"] * 100, 200, 50))
        font = pygame.font.Font(None, 38)
        texto = font.render(boton["text"], True, "black")
        screen.blit(texto, (430, boton["id"] * 100 + 10))        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               if botones[1]["selected"]==True:
                        running = False
            elif event.key == pygame.K_DOWN:
                id = 0
                for boton in botones:
                    if boton["selected"] == True:
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
                    if boton["selected"] == True:
                        id = boton["id"]
                        boton["selected"] = False
                if id == 1:
                    botones[-1]["selected"] = True
                else:
                    for boton in botones:
                        if boton["id"] == id - 1:
                            boton["selected"] = True
                            break
    

    screen.fill('black')
    dibujar_botones()
    pygame.display.flip()
    clock.tick(60)