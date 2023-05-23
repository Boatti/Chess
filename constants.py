import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800
BOARD = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Game | Boatti")

fps = 60

screen.fill((20, 67, 82))

golosFontBlack = "assets/font/GOLOS/GolosText-Black.ttf"
golosFontRegular = "assets/font/GOLOS/GolosText-Regular.ttf"

fontSize = 20
fontTitleSize = 30
fontBlack = pygame.font.Font(golosFontBlack, fontTitleSize)
fontRegular = pygame.font.Font(golosFontRegular, fontSize)

def renderTextWithAntialias(text, font, color):
    
    renderedText = font.render(text, True, color)
    alphaSurface = pygame.Surface(renderedText.get_size(), pygame.SRCALPHA)
    alphaSurface.blit(renderedText, (0, 0))

    finalSurface = pygame.transform.smoothscale(alphaSurface, renderedText.get_size())
    return finalSurface

textWelcome = renderTextWithAntialias("Welcome to Boatti Chess", fontBlack, (255, 255, 255))
textBoardBlack = renderTextWithAntialias("Black", fontRegular, (255, 255, 255))
textBoardWhite = renderTextWithAntialias("White", fontRegular, (255, 255, 255))

screen.blit(textWelcome, (190, 20))
screen.blit(textBoardBlack, (50, 80))
screen.blit(textBoardWhite, (50, 620))

def drawBoard():

    lightTile = (229, 235, 240)
    darkTile = (125, 135, 150)

    tileSize = HEIGHT // 8
    padding = 100

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
    #timer.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawBoard()
    
pygame.quit()



