import pygame as pg
import json, overall
pg.init()


#CONFIG FILE
config = open("config.json")
config = json.load(config)

#with open("config.json", "r") as config:
    #config = json.load(config)

# DISPLAY
fullscreen = 0
if config["Display"]["windowMode"] == 0:
    fullscreen = pg.FULLSCREEN

windowSize = (config["Display"]["width"], config["Display"]["height"])
display = pg.display.set_mode(windowSize, fullscreen)
window = pg.Surface((config["Display"]["width"]//config["Display"]["dynamicRes"], config["Display"]["height"]//config["Display"]["dynamicRes"]))

fps = pg.time.Clock()

#FONT
displayFont = config["Display"]["font"]

#BLIT FPS
def displayFps():
    font = pg.font.Font(displayFont , 18)
    getFps = str(int(fps.get_fps()))
    rendrFps = font.render(getFps, True, (30,200,200))
    display.blit(rendrFps, (5,5))

#EVENTHANDLER
def eventHandler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    #DYNAMIC RES
    surface = pg.transform.scale(window, (windowSize))
    display.blit(surface,(0,0))


    #SHOW FPS
    if config["Display"]["showFps"] == True:
        displayFps()

    pg.display.flip()
    fps.tick(config["Display"]["frameRate"])


#PLAYER EVENTS
overall = overall.Player(pg, config)

#UPDATE LOOP
while True:
    display.fill(0)
    window.fill((30,30,30))
    #=

    overall.playerGun(pg, window, config)
    overall.playerEvent(pg, window)

    overall.placeBlock(pg, window, config)
    overall.gameMap(pg, window)
    overall.enemAi(pg, window)
    #=
    eventHandler()

