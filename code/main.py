
try:
    import sys, os
    import pygame
    from resources import resourcesManager, loadResources
except Exception as e:
    print("Could not import dependecies: %s" % e)

# globals
size = (width, height) = 1080, 720
gamestate = {

}

def handleInput():
    def exit_game():
        sys.exit(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

def drawWorld(screen: pygame.Surface):
    screen.fill((255,255,255))
    screen.blit(resourcesManager["hero"], (width - 60, height - 60))
    screen.blit(resourcesManager["eviltwin"], (20, 20))

    waterSurface: pygame.Surface = resourcesManager["water"]
    ncols = int(width / waterSurface.get_rect().width)
    nrows = int(height / waterSurface.get_rect().height)
    rotateWater = pygame.transform.rotate(waterSurface, 45)
    pygame.draw.line(screen, (0, 0, 255), (0, height), (width, 0), 32)
    # for i in range(ncols):
        # pygame.draw.line(screen,( i * waterSurface.get_rect().width, height - i * waterSurface.get_rect().height))
        # screen.blit(rotateWater,( i * waterSurface.get_rect().width, height - i * waterSurface.get_rect().height))



def main(gamepath):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Evil Twin")
    clock = pygame.time.Clock()

    loadResources(gamepath)


    while (True):
        timePassed = clock.tick(60)
        handleInput()
        drawWorld(screen)
        pygame.display.flip()
