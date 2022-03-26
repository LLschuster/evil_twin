
try:
    import sys
    import pygame
    from resources import resourcesManager, loadResources
    from world import drawWorld, loadLevel, Tile, drawEnemies, Enemy
    from constants import width, height, size
    from util import Vector2
    from gameState import GameState, GameCamera, Player, drawPlayer
except Exception as e:
    print("Could not import dependecies: %s" % e)


gameState = GameState()

def handleInput():
    def exit_game():
        sys.exit(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game()
            if event.key == pygame.K_SPACE:
                print("toggle pause")
                gameState.pause = not gameState.pause
            if gameState.pause:
                return
            if event.key == pygame.K_LEFT:
                print("moving left")
                gameState.gameCamera.move("left")
            if event.key == pygame.K_DOWN:
                print("moving down")
                gameState.gameCamera.move("down")
            if event.key == pygame.K_RIGHT:
                print("moving right")
                gameState.gameCamera.move("right")
            if event.key == pygame.K_UP:
                print("moving up")
                gameState.gameCamera.move("up")
            if event.key == pygame.K_a:
                print("moving left")
                gameState.player.move("left")
            if event.key == pygame.K_s:
                print("moving down")
                gameState.player.move("down")
            if event.key == pygame.K_d:
                print("moving right")
                gameState.player.move("right")
            if event.key == pygame.K_w:
                print("moving up")
                gameState.player.move("up")


def main(gamepath):
    pygame.init()
    global gameState
    gameState.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Evil Twin")
    clock = pygame.time.Clock()

    loadResources(gamepath)

    maxCameraX, maxCameraY = loadLevel(1, gameState )

    gameState.gameCamera = GameCamera(Vector2(width // 2, height // 2), maxCameraX, maxCameraY)
    gameState.player = Player(Vector2(0, 0), resourcesManager["hero"])

    while (True):
        timePassed = clock.tick(60)
        handleInput()
        drawWorld(gameState)
        drawPlayer(gameState)
        drawEnemies(gameState)
        pygame.display.flip()
