import pygame, os

def startGame():
    run = True
    while run:
        
        pygame.init()
        win = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hotel Operations")

def drawText(screen, text, x, y, font, color):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    screen.blit(textSurface, textRect)
