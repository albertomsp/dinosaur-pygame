"""
This is the first version I made when I was in the 2nd year of my studies.
"""
import pygame
from pygame.locals import *
import random
import time
from random import randint
from random import randrange


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
puntuacion = 0

# NOTA: Para hacer lo de los niveles creo que es mejor en vez de poner
# contadorMeteoritos > 15, sustituir el
# 15 por una vble y cambiarla cada nivel


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dinosaurio")
    fondo_image, fondo_rect = load_image("images/fondo.jpg")
    screen.blit(fondo_image, (0, 0))
    pygame.mouse.set_visible(False)

    dinosaurioSprite = pygame.sprite.RenderClear()
    sdinosaurio = dinosaurio(SCREEN_HEIGHT - 22)
    dinosaurioSprite.add(sdinosaurio)

    meteoritosSprite = pygame.sprite.RenderClear()
    meteoritosSprite.add(meteorito(40))
    meteoritosSprite.add(meteorito(300))
    meteoritosSprite.add(meteorito(560))

    jamonSprite = pygame.sprite.RenderClear()

    meteoritoGordoSprite = pygame.sprite.RenderClear()

    clock = pygame.time.Clock()
    contadorMeteoritos = 0
    contadorJamon = 0
    contadorMeteoritoGordo = 0

    # puntuacion("imagen")
    # imagenpuntuacion = pygame.font.Font.render('0000',False,(0,0,255))

    nivel = 0
    contadorNivel = 0

    while 1:
        clock.tick(60)

        pygame.event.pump()
        sdinosaurio.mover_raton()

        if contadorNivel == nivel * 1000:
            nivel += 1
            # puntuacion = 1000 # 1000 puntos por pasar de nivel
            print('nuevonivel')

        if contadorMeteoritos > 30:
            contadorMeteoritos = 0
            meteoritosSprite.add(meteorito(random.randint(5, 590)))
            # puntuacion += 10 #10 puntos por cada meteorito

        # En el contadorJamon se puede poner algo para el nivel, por ejemplo
        # contadorJamon == nivel * 50 o algo por el estilo
        if contadorJamon == 100:
            contadorJamon = 0
            jamonSprite.add(jamon(random.randint(5, 590)))
            # puntuacion += 50
        else:
            contadorJamon += 1

        if contadorMeteoritoGordo >= 20:
            contadorMeteoritoGordo = 0
            meteoritoGordoSprite.add(meteoritoGordo(random.randint(5, 590)))
            # puntuacion += 20
        else:
            contadorMeteoritoGordo += 1

        contadorNivel += 1

        # Actualizamos todos los sprites (sin mostrar los cambios por pantalla
        meteoritosSprite.update()
        dinosaurioSprite.update()
        jamonSprite.update()
        meteoritoGordoSprite.update()

        # Miramos a ver si algun meteorito le ha dado al dinosaurio
        # Si pone un 1 el objeto se destruye y si pones un 0 el objeto sigue vivo
        # (ponemos un 0 para el dinosaurio y un 1 para el grupo de meteoritos)
        for hit in pygame.sprite.groupcollide(dinosaurioSprite, meteoritosSprite, 0, 1):
            for din in dinosaurioSprite:
                din.collision()
        # Comprobamos si el dinosaurio 'come' un jamon
        for hit in pygame.sprite.groupcollide(dinosaurioSprite, jamonSprite, 0, 1):
            for din in dinosaurioSprite:
                din.collisionJamon()
        # Comprobamos si un meteorito gordo le da al dinosaurio
        for hit in pygame.sprite.groupcollide(dinosaurioSprite, meteoritoGordoSprite, 0, 1):
            for din in dinosaurioSprite:
                din.collisionMeteoritoGordo()

        # Limpiamos todo lo que fue pintado por ultima vez
        meteoritosSprite.clear(screen, fondo_image)
        dinosaurioSprite.clear(screen, fondo_image)
        jamonSprite.clear(screen, fondo_image)
        meteoritoGordoSprite.clear(screen, fondo_image)

        # Pinta todo
        meteoritosSprite.draw(screen)
        dinosaurioSprite.draw(screen)
        jamonSprite.draw(screen)
        meteoritoGordoSprite.draw(screen)

        # Eventos para salir del juego
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[K_ESCAPE] or pygame.event.peek(QUIT):
            raise SystemExit

        contadorMeteoritos = contadorMeteoritos + 1 + nivel

        time.sleep(20.0 / 1000.0)

        # Se redibuja el fondo y se actualizan las imagenes

        pygame.display.flip()


def load_image(nombre, colorkey=False):
    try:
        image = pygame.image.load(nombre)
    except pygame.error as message:
        print('No se puede cargar la imagen ', name)
        raise(SystemExit, message)

    image = image.convert_alpha()
    # if(colorkey):
    #     colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class dinosaurio(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/dinosaurio.png")
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = y
        self.vidas = 5
        self.puntuacion = 0

    def mover_raton(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def collision(self):
        self.vidas -= 1
        print(self.vidas)
        if self.vidas == 0:
            print('Has perdido')
            print("puntuacion: " + str(puntuacion))
            raise SystemExit

    def collisionJamon(self):
        self.vidas += 1
        print(self.vidas)

    def collisionMeteoritoGordo(self):
        self.vidas -= 2
        print(self.vidas)
        if self.vidas <= 0:
            print('Has perdido')
            print("puntuacion: " + str(puntuacion))
            raise SystemExit


class meteorito(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/meteorito.png")
        self.rect.centerx = x
        self.rect.centery = 5
        # self.speed = [-1, 6]
        self.speed = [randint(-2, 2), randrange(2) + 4]

    def update(self):
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.rect.bottom > SCREEN_HEIGHT:
            # Si voy a poner varios, lo k hay k hacer es self.kill()
            self.kill()


class jamon(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/jamon.png", True)
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [0, 2]

    def update(self):
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.rect.bottom > SCREEN_HEIGHT:
            # Si voy a poner varios, lo k hay k hacer es self.kill()
            self.kill()

class meteoritoGordo(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/meteoritoGordo.png")
        self.rect.centerx = x
        self.rect.centery = 5
        # self.speed = [-1,5]
        self.speed = [randint(-1, 1), randrange(2) + 3]

    def update(self):
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.rect.bottom > SCREEN_HEIGHT:
            # Si voy a poner varios, lo k hay k hacer es self.kill()
            self.kill()


if __name__ == '__main__':
    main()
