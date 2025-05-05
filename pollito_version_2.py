import os
import sys

import pygame

cwd = os.getcwd()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
MARRON = (150, 75, 0)
GRIS = (200, 200, 200)
AMARILLO = (255, 255, 0)

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Salva al pollito")

clock = pygame.time.Clock()

TAMANO_CUADRO = 25


# Tamaño del carro
TAMANO_CARRO_X = 70
TAMANO_CARRO_Y = 50


TAMANO_POLLO_X = 30
TAMANO_POLLO_Y = 30

DIMENSION_CARRO = (TAMANO_CARRO_X, TAMANO_CARRO_Y)
DIMENSION_POLLO = (TAMANO_POLLO_X, TAMANO_POLLO_Y)

# Configura imagen pollo
imagen_pollito = pygame.image.load(f"{cwd}/assets/pollito.png")
imagen_pollito = pygame.transform.scale(imagen_pollito, DIMENSION_POLLO)

# Configura imagen carro
imagen_carro = pygame.image.load("assets/caryellow.webp")
imagen_carro = pygame.transform.scale(imagen_carro, DIMENSION_CARRO)

factor_velocidad = 6


# Clase Carro
class Carro(pygame.sprite.Sprite):
    def __init__(self, color, ubicacion_x, ubucacion_y, direccion, invertir=False):
        super().__init__()
        self.image = imagen_carro  # Aseguramos que la imagen conserve la transparencia
        self.rect = self.image.get_rect()
        self.rect.x = ubicacion_x
        self.rect.y = ubucacion_y
        self.direccion = direccion

        if invertir:
            self.image = pygame.transform.flip(imagen_carro, True, False)

    def update(self):
        # Aumentamos la velocidad cambiando el valor de multiplicación a 4
        self.rect.x += self.direccion * factor_velocidad  # para aumentar la velocidad

        if self.rect.x < -TAMANO_CUADRO:
            self.rect.x = 800

        elif self.rect.x > 800:
            self.rect.x = -TAMANO_CUADRO


# Clase Cuadro Amarillo
class Pollito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = imagen_pollito
        self.rect = self.image.get_rect()

        # ubucacion inicial pollo
        self.rect.x = 400
        self.rect.y = 500
        self.velocidad = 5

    def update(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        # Limitar el movimiento para que no se salga de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 800 - TAMANO_CUADRO:
            self.rect.x = 800 - TAMANO_CUADRO
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 600 - TAMANO_CUADRO:
            self.rect.y = 600 - TAMANO_CUADRO


# Grupos de carros
grupo_carros_superior = pygame.sprite.Group()
grupo_carros_inferior = pygame.sprite.Group()

# Carros arriba (dos carriles)
grupo_carros_superior.add(
    Carro(ROJO, 300, 250, -1),
    Carro(AZUL, 250, 190, -1),
    Carro(VERDE, 200, 245, -1),
    Carro(MARRON, 600, 190, -1),
)

# Carros abajo (dos carriles)
grupo_carros_inferior.add(
    Carro(ROJO, 50, 400, 1, True),
    Carro(AZUL, 200, 340, 1, True),
    Carro(VERDE, 350, 400, 1, True),
    Carro(MARRON, 500, 340, 1, True),
    Carro(GRIS, 650, 400, 1, True),
)

# Crear el cuadro amarillo
pollito = Pollito()

# Grupo de sprites para el cuadro amarillo
grupo_pollito = pygame.sprite.Group()
grupo_pollito.add(pollito)

# Variables de vida
vidas = 5
fuente = pygame.font.SysFont("Arial", 30)

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()
    pollito.update(teclas)

    # Detectar colisiones entre el cuadro amarillo y los carros
    if pygame.sprite.spritecollide(
        pollito, grupo_carros_superior, False
    ) or pygame.sprite.spritecollide(pollito, grupo_carros_inferior, False):
        vidas -= 1  # Reduce la vida en caso de colisión
        pollito.rect.x = 400  # Restablece la posición del cuadro amarillo
        pollito.rect.y = 500
        factor_velocidad += 1  # Aumentar la velocidad del juego

    if vidas <= 0:
        # Mostrar mensaje de fin de juego
        texto_gameover = fuente.render("¡Game Over!", True, ROJO)
        ventana.blit(texto_gameover, (300, 250))
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
        sys.exit()

    ventana.fill(BLANCO)

    # dibujo de la carretera
    carretera = [
        (NEGRO, (0, 150, 800, 330)),
        (GRIS, (0, 310, 800, 10)),
        (ROJO, (0, 150, 800, 20)),
        (ROJO, (0, 470, 800, 20)),
    ]

    for color, dimensiones in carretera:
        pygame.draw.rect(ventana, color, dimensiones)

    # Optimización de la creación de rectángulos con un patrón
    for x in range(30, 734, 70):
        pygame.draw.rect(ventana, BLANCO, (x, 390, 30, 5))
        pygame.draw.rect(ventana, BLANCO, (x, 235, 30, 5))

    # Actualizar y dibujar carros
    grupo_carros_superior.update()
    grupo_carros_inferior.update()
    grupo_carros_superior.draw(ventana)
    grupo_carros_inferior.draw(ventana)

    # Mostrar las vidas restantes
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, NEGRO)
    ventana.blit(texto_vidas, (650, 20))

    # Dibujar el cuadro amarillo
    grupo_pollito.draw(ventana)

    # Dibujar casas en la parte superior blanca
    pygame.draw.rect(ventana, MARRON, (100, 60, 60, 60))

    pygame.draw.rect(ventana, VERDE, (250, 60, 60, 60))

    pygame.draw.rect(ventana, AZUL, (400, 60, 60, 60))

    pygame.display.flip()
