import os, io, pygame
from constants import mapTileSize
from resources import resourcesManager
from util import Vector2
from gameState import Tile, Enemy, GameState

def loadLevel(number, gameState: GameState):
    maxWidth = -1
    maxHeight = -1
    def findPlayerPos():
        with io.open(os.path.join("data", "levels", "%d.txt" % number), mode="r" , encoding="utf-8") as file:
            for (row, line) in enumerate(file):
                for (col, c) in enumerate(line):
                    if c == "P":
                        return col, row

    playerX, playerY = findPlayerPos()


    with io.open(os.path.join("data", "levels", "%d.txt" % number), mode="r" , encoding="utf-8") as file:
        tiles = [Tile(0, 0, resourcesManager["grass128"])]
        print(playerX, playerY)
        for (row, line) in enumerate(file):
            maxHeight = max(row, maxHeight)
            for (col, c) in enumerate(line):
                maxWidth = max(col, maxWidth)
                if c == "S":
                    entityPos = Vector2((col - playerX) * mapTileSize, (row - playerY) * mapTileSize)
                    tiles.append(Tile((col - playerX) * mapTileSize, (row - playerY) * mapTileSize, resourcesManager["grass128"]))
                    gameState.enemies.append(Enemy(entityPos, resourcesManager["soldier"]))
                if c == "D":
                    entityPos = Vector2((col - playerX) * mapTileSize, (row - playerY) * mapTileSize)
                    tiles.append(Tile((col - playerX) * mapTileSize, (row - playerY) * mapTileSize, resourcesManager["grass128"]))
                    gameState.enemies.append(Enemy(entityPos, resourcesManager["dragon"]))
                if c == "x":
                    tiles.append(Tile((col - playerX) * mapTileSize, (row - playerY) * mapTileSize, resourcesManager["grass128"]))
                if c == "w":
                    tiles.append(Tile((col - playerX) * mapTileSize, (row - playerY) * mapTileSize, resourcesManager["crystal128"]))

        gameState.tiles = tiles
    
    return maxWidth * mapTileSize, maxHeight * mapTileSize

def drawWorld(gameState: GameState):
    gameState.screen.fill((0,0,0))

    # print(gameState.tiles)
    for tile in gameState.tiles:
        screenPosX = gameState.gameCamera.position.x + tile.position.x
        screenPosY = gameState.gameCamera.position.y + tile.position.y

        print("drawing tile: ")
        print(screenPosX, screenPosY)
        gameState.screen.blit(tile.texture, (screenPosX, screenPosY))

def drawEnemies(gameState: GameState):
    for enemy in gameState.enemies:
        screenPosX = gameState.gameCamera.position.x + enemy.position.x
        screenPosY = gameState.gameCamera.position.y + enemy.position.y
        gameState.screen.blit(enemy.texture, (screenPosX, screenPosY))