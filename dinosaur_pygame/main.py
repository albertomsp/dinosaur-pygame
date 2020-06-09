import pygame
from pygame.locals import *
import random
import time
from random import randint
from random import randrange
import os.path

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
score = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dinosaur RAWR!')
    background_image, background_rect = _load_image('./images/background.png')
    screen.blit(background_image, (0, 0))
    pygame.mouse.set_visible(False)

    dinosaur_sprite = pygame.sprite.RenderClear()
    dinosaur = Dinosaur(SCREEN_HEIGHT - 22)
    dinosaur_sprite.add(dinosaur)

    meteors_sprite = pygame.sprite.RenderClear()
    meteors_sprite.add(Meteor(40))
    meteors_sprite.add(Meteor(300))
    meteors_sprite.add(Meteor(560))

    ham_sprite = pygame.sprite.RenderClear()

    big_meteor_sprite = pygame.sprite.RenderClear()

    clock = pygame.time.Clock()
    meteor_counter = 0
    ham_counter = 0
    big_meteor_counter = 0

    # score('image')
    # score_image = pygame.font.Font.render('0000',False,(0,0,255))

    level = 0
    level_counter = 0

    while 1:
        clock.tick(60)

        pygame.event.pump()
        dinosaur.move_with_mouse()

        if level_counter == level * 1000:
            level += 1
            # score = 1000 # 1000 puntos por pasar de level
            print('New Level')

        if meteor_counter > 30:
            meteor_counter = 0
            meteors_sprite.add(Meteor(random.randint(5, 590)))
            # score += 10 # 10 points for each dodged meteor

        if ham_counter == 100:
            ham_counter = 0
            ham_sprite.add(Ham(random.randint(5, 590)))
            # score += 50
        else:
            ham_counter += 1

        if big_meteor_counter >= 20:
            big_meteor_counter = 0
            big_meteor_sprite.add(BigMeteor(random.randint(5, 590)))
            # score += 20
        else:
            big_meteor_counter += 1

        level_counter += 1

        # Update every sprite (not showing the update in the screen yet)
        meteors_sprite.update()
        dinosaur_sprite.update()
        ham_sprite.update()
        big_meteor_sprite.update()

        # 1 if the object is destroyed, 0 if the object keeps living:
        # Check if any meteor or ham has hit the dinosaur.
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, meteors_sprite, 0, 1):
            for din in dinosaur_sprite:
                din.meteor_collision()
        # Check if any big meteor has hit the dinosaur.
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, big_meteor_sprite, 0, 1):
            for din in dinosaur_sprite:
                din.big_meteor_collision()
        # Check if the dinosaur has eaten a ham
        for hit in pygame.sprite.groupcollide(dinosaur_sprite, ham_sprite, 0, 1):
            for din in dinosaur_sprite:
                din.ham_collision()

        # Clears everything that is out of date in this iteration of the loop
        meteors_sprite.clear(screen, background_image)
        dinosaur_sprite.clear(screen, background_image)
        ham_sprite.clear(screen, background_image)
        big_meteor_sprite.clear(screen, background_image)

        # Draws everything that has changed in this iteration of the loop
        meteors_sprite.draw(screen)
        dinosaur_sprite.draw(screen)
        ham_sprite.draw(screen)
        big_meteor_sprite.draw(screen)

        # Events to exit the game
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[K_ESCAPE] or pygame.event.peek(QUIT):
            raise SystemExit

        meteor_counter = meteor_counter + 1 + level

        time.sleep(20.0 / 1000.0)

        # Re-draw everything and update the images
        pygame.display.flip()


def _load_image(relative_image_path, colorkey=False):
    """ Utility method to load the images. It handles if the images contain
    transparency.
    """
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_image_path = os.path.join(current_path, relative_image_path)

    image = pygame.image.load(absolute_image_path).convert_alpha()
    return image, image.get_rect()


class Dinosaur(pygame.sprite.Sprite):
    """ Class that handles all of the logic of the Player (Dinosaur)
    """

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = _load_image('./images/dinosaur.png')
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = y
        self.current_lives = 5
        self.score = 0

    def move_with_mouse(self):
        """ Handles the movement of the dinosaur when the mouse is moved.
        """
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def update_current_lives(self, lives_change):
        """ Adds or removes from `self.current_lives` as many lives specified
        in lives_change.
        """
        self.current_lives += lives_change
        print(self.current_lives)

        if self.current_lives <= 0:
            print('You Lost')
            print('score: ' + str(score))
            raise SystemExit

    def meteor_collision(self):
        """ Removes 1 live when hit by a big meteor.
        """
        self.update_current_lives(-1)

    def ham_collision(self):
        """ Adds 1 live when the dinosaur eats a ham.
        """
        self.update_current_lives(1)

    def big_meteor_collision(self):
        """ Removes 2 lives when hit by a big meteor.
        """
        self.update_current_lives(-2)


class FlyingObject(pygame.sprite.Sprite):
    """ Parent class of every object that falls from the sky
    """

    def update(self):
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.rect.bottom > SCREEN_HEIGHT:
            # Si voy a poner varios, lo k hay k hacer es self.kill()
            self.kill()


class Meteor(FlyingObject):
    """ Class for one of the "enemies".
    """

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = _load_image('./images/meteor.png')
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [randint(-2, 2), randrange(2) + 4]


class BigMeteor(FlyingObject):
    """ Class for one of the "enemies".
    """

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = _load_image('./images/meteor-big.png')
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [randint(-1, 1), randrange(2) + 3]


class Ham(FlyingObject):
    """ Class for a power up that gives a life to the player if eaten.
    """

    def __init__(self, x):
        FlyingObject.__init__(self)
        self.image, self.rect = _load_image('./images/ham.png', True)
        self.rect.centerx = x
        self.rect.centery = 5
        self.speed = [0, 2]


if __name__ == '__main__':
    main()
