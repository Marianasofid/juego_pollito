import pygame
import sys

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

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Salva al pollito")

clock = pygame.time.Clock()

# Tamaño del carro
TAMANO_CARRO = 40
TAMANO_CUADRO = 25  

# Clase Carro
class Carro(pygame.sprite.Sprite):
    def __init__(self, color, x, y, direccion):
        super().__init__()
        self.image = pygame.Surface((TAMANO_CARRO, TAMANO_CARRO))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = direccion

    def update(self):
        # Aumentamos la velocidad cambiando el valor de multiplicación a 4
        self.rect.x += self.direccion * 8  # para aumentar la velocidad
        if self.rect.x < -TAMANO_CARRO:
            self.rect.x = 800
        elif self.rect.x > 800:
            self.rect.x = -TAMANO_CARRO

# Clase Cuadro Amarillo
class CuadroAmarillo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TAMANO_CUADRO, TAMANO_CUADRO))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
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
    Carro(MARRON, 600, 190, -1)
)

# Carros abajo (dos carriles)
grupo_carros_inferior.add(
    Carro(ROJO, 50, 400, 1),
    Carro(AZUL, 200, 340, 1),
    Carro(VERDE, 350, 400, 1),
    Carro(MARRON, 500, 340, 1),
    Carro(GRIS, 650, 400, 1)
)

# Crear el cuadro amarillo
cuadro_amarillo = CuadroAmarillo()

# Grupo de sprites para el cuadro amarillo
grupo_cuadro_amarillo = pygame.sprite.Group()
grupo_cuadro_amarillo.add(cuadro_amarillo)

# Variables de vida
vidas = 3
fuente = pygame.font.SysFont("Arial", 30)

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()
    cuadro_amarillo.update(teclas)

    # Detectar colisiones entre el cuadro amarillo y los carros
    if pygame.sprite.spritecollide(cuadro_amarillo, grupo_carros_superior, False) or pygame.sprite.spritecollide(cuadro_amarillo, grupo_carros_inferior, False):
        vidas -= 1  # Reduce la vida en caso de colisión
        cuadro_amarillo.rect.x = 400  # Restablece la posición del cuadro amarillo
        cuadro_amarillo.rect.y = 500

    if vidas <= 0:
        # Mostrar mensaje de fin de juego
        texto_gameover = fuente.render("¡Game Over!", True, ROJO)
        ventana.blit(texto_gameover, (300, 250))
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
        sys.exit()

    ventana.fill(BLANCO)

    # Dibujo de carretera
    pygame.draw.rect(ventana, NEGRO, (0, 150, 800, 330))
    pygame.draw.rect(ventana, GRIS, (0, 310, 800, 10))
    pygame.draw.rect(ventana, ROJO, (0, 150, 800, 20))
    pygame.draw.rect(ventana, ROJO, (0, 470, 800, 20))

    pygame.draw.rect(ventana, BLANCO, (30, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (100, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (170, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (240, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (315, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (390, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (460, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (530, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (600, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (670, 390, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (733, 390, 30, 5))

    pygame.draw.rect(ventana, BLANCO, (30, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (100, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (170, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (240, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (315, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (390, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (460, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (530, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (600, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (670, 235, 30, 5))
    pygame.draw.rect(ventana, BLANCO, (733, 235, 30, 5))

    # Actualizar y dibujar carros
    grupo_carros_superior.update()
    grupo_carros_inferior.update()
    grupo_carros_superior.draw(ventana)
    grupo_carros_inferior.draw(ventana)

    # Mostrar las vidas restantes
    texto_vidas = fuente.render(f'Vidas: {vidas}', True, NEGRO)
    ventana.blit(texto_vidas, (650, 20))

    # Dibujar el cuadro amarillo
    grupo_cuadro_amarillo.draw(ventana)

    # Dibujar casas en la parte superior blanca
    pygame.draw.rect(ventana, MARRON, (100, 60, 60, 60))
    pygame.draw.polygon(ventana, ROJO, [(100, 60), (130, 30), (160, 60)])
    pygame.draw.rect(ventana, NEGRO, (125, 90, 10, 30))

    pygame.draw.rect(ventana, VERDE, (250, 60, 60, 60))
    pygame.draw.polygon(ventana, ROJO, [(250, 60), (280, 30), (310, 60)])
    pygame.draw.rect(ventana, NEGRO, (275, 90, 10, 30))

    pygame.draw.rect(ventana, AZUL, (400, 60, 60, 60))
    pygame.draw.polygon(ventana, ROJO, [(400, 60), (430, 30), (460, 60)])
    pygame.draw.rect(ventana, NEGRO, (425, 90, 10, 30))

    pygame.display.flip()