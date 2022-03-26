
import pygame, os

resourcesManager = {}

def loadResources(gamepath):
    
    def loadBlastFrames():
        blastFrames = []
        for i in range(1, 6):
            currentFrame = pygame.image.load(os.path.join(gamepath, "data", "g", "blast00%d.png" % i))
            blastFrames.append(currentFrame)
        resourcesManager["blast"] = blastFrames

    def loadBuildings():
        buildingFrames = []
        for i in range(1, 5):
            currentFrame = pygame.image.load(os.path.join(gamepath, "data", "g", "human-city%d.png" % i))
            buildingFrames.append(currentFrame)
        resourcesManager["buildings"] = buildingFrames

    resourcesManager["dragon"] = pygame.image.load(os.path.join(gamepath, "data", "g", "dragon.png")).convert_alpha()
    resourcesManager["eviltwin"] = pygame.image.load(os.path.join(gamepath, "data", "g", "eviltwin.png")).convert_alpha()
    resourcesManager["goblin"] = pygame.image.load(os.path.join(gamepath, "data", "g", "goblin1.png"))
    resourcesManager["hero"] = pygame.image.load(os.path.join(gamepath, "data", "g", "hero.png")).convert_alpha()
    resourcesManager["wolf"] = pygame.image.load(os.path.join(gamepath, "data", "g", "wolf.png"))
    resourcesManager["soldier"] = pygame.image.load(os.path.join(gamepath, "data", "g", "soldier.png"))
    resourcesManager["water"] = pygame.image.load(os.path.join(gamepath, "data", "g", "water.png"))
    resourcesManager["grass"] = pygame.image.load(os.path.join(gamepath, "data", "g", "grass.png"))
    resourcesManager["grass128"] = pygame.image.load(os.path.join(gamepath, "data", "g", "grass128.png"))
    resourcesManager["lighthouse"] = pygame.image.load(os.path.join(gamepath, "data", "g", "lighthouse.png"))

    resourcesManager["skull"] = pygame.image.load(os.path.join(gamepath, "data", "g", "skull1.png"))
    resourcesManager["crystal"] = pygame.image.load(os.path.join(gamepath, "data", "g", "crystal1.png"))
    resourcesManager["crystal128"] = pygame.image.load(os.path.join(gamepath, "data", "g", "crystal128.png"))
    resourcesManager["iron"] = pygame.image.load(os.path.join(gamepath, "data", "g", "iron1.png"))
    resourcesManager["coin"] = pygame.image.load(os.path.join(gamepath, "data", "g", "coin1.png"))

    loadBlastFrames()
    loadBuildings()