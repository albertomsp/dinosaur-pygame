import pygame
from pygame.locals import *
import random
import time
from random import randint
from random import randrange


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
score = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dinosaur RAWR!")
    background_image, background_rect = load_image("images/background.png")
    screen.blit(background_image, (0, 0))
    pygame.mouse.set_visible(False)

    dinosaur_sprite = pygame.sprite.RenderClear()
    dinosaur = Dinosaur(SCREEN_HEIGHT - 22)
    dinosaur_sprite.add(dinosaur)

    meteors_sprite = pygame.sprite.RenderClear()
    meteors_sprite.add(Meteor(40))
    meteors_sprite.add(Meteor(300))
    meteors_sprite.add(Meteor(560))

    jamonSprite = pygame.sprite.RenderClear()

    big_meteor_sprite = pygame.sprite.RenderClear()

    clock = pygame.time.Clock()
    contadorMeteoritos = 0
    contadorJamon = 0
    contadorMeteoritoGordo = 0

    # score("imagen")
    # imagenpuntuacion = pygame.font.Font.render('0000',False,(0,0,255))

    nivel = 0
    contadorNivel = 0

    while 1:
        clock.tick(60)

        pygame.event.pump()
        dinosaur.mover_raton()

        if contadorNivel == nivel * 1000:
            nivel += 1
            # score = 1000 # 1000 puntos por pasar de nivel
            print('nuevonivel')

        if contadorMeteoritos > 30:
            contadorMeteoritos = 0
            meteors_sprite.add(Meteor(random.randint(5, 590)))
            # score += 10 #10 puntos por cada meteorito

        # En el contadorJamon se puede poner algo para el nivel, por ejemplo
        # contadorJamon == nivel * 50 o algo por el estilo
        if contadorJamon == 100:
            contadorJamon = 0
            jamonSprite.add(jamon(random.randint(5, 590)))
            # score += 50
        else:
            contadorJamon += 1

        if contadorMeteoritoGordo >= 20:
            contadorMeteoritoGordo = 0
            big_meteor_sprite.add(BigMeteor(random.randint(5, 590)))
            # score += 20
        else:
            contadorMeteoritoGordo += 1

        contadorNivel += 1

        # Actualizamos todos los sprites (sin mostrar los cambios por pantalla
        meteors_sprite.update()
        dinosaur_sprite.update()
        jamonSprite.update()
        big_meteor_sprite.update()

        # Miramos a ver si algun meteorito le ha dado al dinosaur
        # Si pone un 1 el objeto se destruye y si pones un 0 el objeto sigue vivo
        # (ponemos un 0 para el dinosaur y un 1 para el grupo de meteoritos)
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, meteors_sprite, 0, 1):
            for din in dinosaur_sprite:
                din.collision()
        # Comprobamos si el dinosaur 'come' un jamon
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, jamonSprite, 0, 1):
            for din in dinosaur_sprite:
                din.collisionJamon()
        # Comprobamos si un meteorito gordo le da al dinosaur
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, big_meteor_sprite, 0, 1):
            for din in dinosaur_sprite:
                din.collisionMeteoritoGordo()

        # Limpiamos todo lo que fue pintado por ultima vez
        meteors_sprite.clear(screen, background_image)
        dinosaur_sprite.clear(screen, background_image)
        jamonSprite.clear(screen, background_image)
        big_meteor_sprite.clear(screen, background_image)

        # Pinta todo
        meteors_sprite.draw(screen)
        dinosaur_sprite.draw(screen)
        jamonSprite.draw(screen)
        big_meteor_sprite.draw(screen)

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

class Dinosaur(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/dinosaur.png")
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = y
        self.vidas = 5
        self.score = 0

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
            print("score: " + str(score))
            raise SystemExit

    def collisionJamon(self):
        self.vidas += 1
        print(self.vidas)

    def collisionMeteoritoGordo(self):
        self.vidas -= 2
        print(self.vidas)
        if self.vidas <= 0:
            print('Has perdido')
            print("score: " + str(score))
            raise SystemExit


class FlyingObject(pygame.sprite.Sprite):

    def update(self):
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.rect.bottom > SCREEN_HEIGHT:
            # Si voy a poner varios, lo k hay k hacer es self.kill()
            self.kill()

class Meteor(FlyingObject):

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = load_image("images/meteor.png")
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [randint(-2, 2), randrange(2) + 4]


class BigMeteor(FlyingObject):

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = load_image("images/meteor-big.png")
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [randint(-1, 1), randrange(2) + 3]



class jamon(FlyingObject):

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = load_image("images/ham.png", True)
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [0, 2]


if __name__ == '__main__':
    main()
