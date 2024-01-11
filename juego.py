import pygame, os

class pelota:
    def __init__(self):
        self.image_vida=pelota=pygame.image.load(os.path.join(os.path.dirname(__file__),"Image","barra.png"))
        self.rect=self.image_vida.get_rect()
        self.rect.move_ip(500,10)
pygame.init()
size=(1000,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Juego tilin")
clock=pygame.time.Clock()
running=True
black=(255,255,255)
mov_x=10
mov_y=10
speed_x=3
speed_y=3
veces=0
fondo=pygame.image.load(os.path.join(os.path.dirname(__file__),"Image","Hasganado.png")).convert()
hasperdido=pygame.image.load(os.path.join(os.path.dirname(__file__),"Image","Hasganado.png")).convert()
def boton():
    boton=pygame.draw.rect(screen, (255,255,255), (150,100,100,50))
    font = pygame.font.Font(None, 36)
    texto = font.render("Volver", True, "black")
    screen.blit(texto, (100,100))
    return boton
while running:
    zaz=False
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(event.pos):
                mov_x=0
                mov_y=0
                veces=0
        elif event.type== pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                mov_x=0
                mov_y=0
                veces=0
    screen.fill('black')
    coordenates=pygame.mouse.get_pos()
    distance = ((mov_x - coordenates[0])**2 + (mov_y - coordenates[1])**2)**0.5
    pygame.draw.circle(screen,black if distance>=20 else (255,0,0),(mov_x,mov_y),20)
    if distance<=20:
        veces+=1
    if veces>=100:
        screen.blit(hasperdido, (250, 264))
        boton_rect=boton()
    mov_y+=speed_y
    mov_x+=speed_x
    if mov_x>=size[0] or mov_x<0:
        speed_x*=-1
    if mov_y>=size[1] or mov_y<0:
        speed_y*=-1
    pygame.display.flip()
    clock.tick(60)  
