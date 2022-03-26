import pygame
from constants import width, height
from util import Vector2, clamp


class Tile(object):
    def __init__(self, x, y, texture):
        super()
        self.position = Vector2(x, y)
        self.type = type
        self.maxX = width - 60
        self.maxY = height - 60
        self.texture = texture

class Enemy(object):
    def __init__(self, pos: Vector2, texture):
        self.velocity = 20
        self.position = pos
        self.type = type
        self.maxX = width - 60
        self.maxY = height - 60
        self.texture = texture

class GameCamera(object):
    def __init__(self, pos: Vector2, maxX, maxY):
        self.position = pos
        self.velocity = 128
        self.maxX = maxX
        self.maxY = maxY

    def move(self, direction):
        if direction == "up":
            self.position.y += self.velocity
        if direction == "down":
            self.position.y -= self.velocity
        if direction == "left":
            self.position.x -= self.velocity
        if direction == "right":
            self.position.x += self.velocity
        self.position.x = clamp(self.position.x, 0, self.maxX)
        self.position.y = clamp(self.position.y, 0, self.maxY)

class Player(object):
    def __init__(self, pos: Vector2, texture):
        self.velocity = 20
        self.position = pos
        self.maxX = width - 60
        self.maxY = height - 60
        self.texture = texture

    def move(self, direction):
        if direction == "up":
            self.position.y -= self.velocity
        if direction == "down":
            self.position.y += self.velocity
        if direction == "left":
            self.position.x -= self.velocity
        if direction == "right":
            self.position.x += self.velocity

class GameState:
    def __init__(self):
        pass
    screen: pygame.Surface = None
    player: Player = None
    gameCamera: GameCamera = None
    pause: bool = False
    enemies: list[Enemy] = []
    tiles: list[Tile] = []
    world: list[list[str]] = [[]]

def drawPlayer(gameState: GameState):
        screenPosX = gameState.gameCamera.position.x + gameState.player.position.x
        screenPosY = gameState.gameCamera.position.y + gameState.player.position.y
        gameState.screen.blit(gameState.player.texture, (screenPosX, screenPosY))
    

