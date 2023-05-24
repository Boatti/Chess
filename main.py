import pygame
from chessGame.constants import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Game | Boatti")
screen.fill((20, 67, 82))

#FONT---
fontBlack = pygame.font.Font(golosFontBlack, fontTitleSize)
fontRegular = pygame.font.Font(golosFontRegular, fontSize)

def renderTextWithAntialias(text, font, color):
    
    renderedText = font.render(text, True, color)
    alphaSurface = pygame.Surface(renderedText.get_size(), pygame.SRCALPHA)
    alphaSurface.blit(renderedText, (0, 0))

    finalSurface = pygame.transform.smoothscale(alphaSurface, renderedText.get_size())
    return finalSurface

textWelcome = renderTextWithAntialias("Welcome to Boatti Chess", fontBlack, (255, 255, 255))
textBoardBlack = renderTextWithAntialias("-Black-", fontRegular, (255, 255, 255))
textBoardWhite = renderTextWithAntialias("-White-", fontRegular, (255, 255, 255))

screen.blit(textWelcome, (200, 15))
screen.blit(textBoardBlack, (65, 54))
screen.blit(textBoardWhite, (663, 720))
#FONT---

def drawBoard():

    lightTile = (229, 235, 240)
    darkTile = (14, 92, 35)

    tileSize = BOARD // 8
    padding = 80

    for row in range(8):
        for col in range(8):
            x = padding + col * tileSize
            y = padding + row * tileSize
            if (row + col) % 2 == 0:
                color = lightTile
            else:
                color = darkTile
            pygame.draw.rect(screen, color, (x, y, tileSize, tileSize))
    
    
    pygame.display.flip()

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawBoard()
    
pygame.quit()
