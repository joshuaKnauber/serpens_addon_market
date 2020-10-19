import pygame
import os
import sys
from pipe import Pipe
from background import Background

class FlappyBird():
    def __init__(self):
        pass

    def collidedOnX(self, pipe, pipeNumber):
        if pipe.pipePosition()[0][pipeNumber] <= 375+102:
            if pipe.pipePosition()[0][pipeNumber] + 220 >= 375:
                return True
        else:
            return False

    def collidedOnY(self, birdY, pipe, pipeNumber):
        yposition = pipe.pipePosition()[1][pipe.pipePosition()[2][pipeNumber]]
        if birdY < yposition[1]:
            return True
        elif birdY+72 > yposition[0]:
            return True
        else:
            return False

    def collided(self, birdY, firstPipe, secondPipe):
        if self.collidedOnX(firstPipe, 0):
            if self.collidedOnY(birdY, firstPipe, 0):
                return True
        elif self.collidedOnX(secondPipe, 1):
            if self.collidedOnY(birdY, secondPipe, 1):
                return True
        else:
            return False

    def outOfFrame(self, birdY):
        if birdY > 859-72:
            return True
        elif birdY < 0:
            return True
        else:
            return False

    def gravity(self, birdY, jump):
        if jump:
            birdY-=15
        else:
            birdY+=6
        return birdY

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((1000, 859))
        pygame.display.set_caption("Flappy Bird")
        pygame.mouse.set_visible(1)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(50)
        bird = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bird.png'))
        bird = pygame.transform.scale(bird, (108, 72))
        pipe = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pipe.png'))
        reversedPipe = pygame.transform.rotate(pipe, 180)
        background = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background.png'))
        background_size = background.get_size()
        bird_size = bird.get_size()
        birdX = 375
        birdY = 15

        start = False
        jump = False

        firstPipe = Pipe()
        secondPipe = Pipe()
        BackgroundClass = Background(background_size)
        
        # game runs while running is true
        running = True
        while running:
            # game runs at 60 frames 
            clock.tick(60)

            # event handling
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    start = True
                    jump = True

                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running = False

                # if quit stop the game
                if event.type == pygame.QUIT:
                    running = False

            BackgroundClass.display(screen, background, background_size)
            screen.blit(bird,(birdX,birdY))

            if start:
                firstPipe.displayPipes(pipe, reversedPipe, screen, 0)
                secondPipe.displayPipes(pipe, reversedPipe, screen, 1)
                if self.collided(birdY, firstPipe, secondPipe):
                    running = False

                if self.outOfFrame(birdY): 
                    running = False

                birdY = self.gravity(birdY, jump)
                jump = False

            pygame.display.flip()

if __name__ == "__main__":
    fb = FlappyBird()
    fb.display()