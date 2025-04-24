import pygame
import sys



blanco = (255,255,255)
negro = (0,0,0)
pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Salva al pollito")

clock = pygame.time.Clock()

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

    pygame.draw.rect(ventana, blanco, ((50,50), (400,400)), 1)



ventana.fill(blanco)




















pygame.display.flip()
