import pygame
import time
import random
import math

pygame.init()

white = (255,255,255)
black = (0,0,0,)
red = (255,0,0)
green = (0,155,0)


pixel = 15
FPS = 20

dimX = 800
dimY = 600
display_width = dimX - (dimX % pixel)
display_height = dimY - (dimY % pixel)



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# Game display dimensions
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

# Prints message to screen
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [round(display_width/2),round(display_height/2)])

# Draws snake
def snake(snakeList, pixel):
    for XY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XY[0], XY[1], pixel, pixel])

def gameLoop():
# Spawns pixel in center of display
    lead_x = dimX/2 - (dimX/2 % pixel)
    lead_y = dimY/2 - (dimY/2 % pixel)
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    gameExit = False
    gameOver = False

# Coordinates for random appple
    randAppleX = math.floor(random.randrange(0, display_width)/pixel)*pixel
    randAppleY = math.floor(random.randrange(0, display_height)/pixel)*pixel
    print(randAppleX, randAppleY)

    while not gameExit:

# Boundaries
        if (lead_x >= display_width or lead_x < 0 or
            lead_y >= display_height or lead_y < 0): gameOver = True

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over, C to continute, Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -pixel
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = pixel
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = pixel
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -pixel
                    lead_x_change = 0
# increments snake/pixel on screen
        lead_x += lead_x_change
        lead_y += lead_y_change
# Eating apple
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = math.floor(random.randrange(0, display_width)/pixel)*pixel
            randAppleY = math.floor(random.randrange(0, display_height)/pixel)*pixel
            snakeLength += 1

# Draw background
        gameDisplay.fill(white)
# Draw apple
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,pixel,pixel])
# Draw snake/pixel


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(snakeList, pixel)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
gameLoop()
