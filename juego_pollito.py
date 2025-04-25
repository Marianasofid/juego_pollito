import pygame
import sys



blanco = (255,255,255)
negro = (0,0,0)
pygame.init()

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Salva al pollito")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    ventana.fill(blanco)

    pygame.display.flip()
