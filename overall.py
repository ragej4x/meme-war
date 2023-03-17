import json
import math 

class Player():
    def __init__(self, pg, config,):
        self.__char_1 = pg.image.load("data/player/__char_1.png")

        self.x = 100
        self.y = 100

        self.pSpeed = 3

        self.walkList = []
        self.animFrame = 0


        #GUN
        self.bullet = []
        self.bulletSpeed = 20
        self.bulX = self.x
        self.bulY = self.y


        #MAP
        self.block = []



        #ENEMY
        self.enemyList = []
        self.enemyX = 0
        self.enemyY = 0

        #CAMERA
        self.cameraX = self.x
        self.cameraY = self.y

    def playerEvent(self, pg, window):
        

        self.keyinput = pg.key.get_pressed()
        self.playerRect = pg.Rect(self.x , self.y, 16,25)
        pg.draw.rect(window, (255,255,255), (self.playerRect))
        self.x = self.playerRect.x
        self.y = self.playerRect.y
        self.center = pg.Rect(self.x, self.y, 1,1)

        self.dx = 0
        self.dy = 0

        #MOVEMENT
        if self.keyinput[pg.K_a]:
            self.dx -= self.pSpeed
            self.center.x -= self.pSpeed
            self.cameraX -= self.pSpeed

        if self.keyinput[pg.K_d]:
            self.dx += self.pSpeed
            self.center.x += self.pSpeed
            self.cameraX += self.pSpeed

        if self.keyinput[pg.K_w]:
            self.dy -= self.pSpeed
            self.center.y -= self.pSpeed
            self.cameraY -= self.pSpeed

        if self.keyinput[pg.K_s]:
            self.dy += self.pSpeed
            self.center.y += self.pSpeed
            self.cameraY += self.pSpeed



    def playerGun(self, pg, window, config):
        
        fire = pg.mouse.get_pressed()[0] 
        mx,my = pg.mouse.get_pos()
        mx // config["Display"]["dynamicRes"]
        my // config["Display"]["dynamicRes"]


        pg.draw.line(window, (30,200,30), (mx// config["Display"]["dynamicRes"], my// config["Display"]["dynamicRes"]),(self.x + 8, self.y))
        pg.draw.circle(window, (200,30,30), (mx// config["Display"]["dynamicRes"], my// config["Display"]["dynamicRes"]), 2)


        if fire:
            self.bullet.append([pg.image.load("data/bulSprite.png") ,  self.center.x + 8, self.center.y,
            mx // config["Display"]["dynamicRes"],
            my // config["Display"]["dynamicRes"],
            math.atan2(self.center.y - my // config["Display"]["dynamicRes"], self.center.x - mx // config["Display"]["dynamicRes"]),
            
            ])


        for bullet in self.bullet:
            bulletRect = bullet[0].get_rect()

            xVel = math.cos(bullet[5]) * self.bulletSpeed
            yVel = math.sin(bullet[5]) * self.bulletSpeed
            
            window.blit(bullet[0], (bullet[1] , bullet[2]))
            
            



    def placeBlock(self, pg, window, config):
        mx,my = pg.mouse.get_pos()
        mx // config["Display"]["dynamicRes"]
        my // config["Display"]["dynamicRes"]

        place = pg.mouse.get_pressed()[2]

        if place:
            self.block.append([pg.Rect(mx // config["Display"]["dynamicRes"], my // config["Display"]["dynamicRes"], 20,20)])

        for block in self.block:
            tile_1 = pg.draw.rect(window, (255,255,255), (block[0]))
            tile_2 = pg.draw.rect(window, (255,255,255), (block[0]))

            if tile_1.colliderect(self.playerRect.x + self.dx, self.playerRect.y, 16,25):
                self.dx = 0

            if tile_1.colliderect(self.playerRect.x, self.playerRect.y + self.dy, 16,25):
                self.dy = 0
                #print("a")

            
    def enemAi(self, pg, window):
        self.enemDx = 0
        self.enemDy = 0
        self.enemRect = pg.Rect(self.enemyX, self.enemyY, 16,25)
        self.enemyList.append([pg.draw.rect(window,(255,0,0), (self.enemRect)) ])


    def gameMap(self, pg, window):
        mapData = open("data/mapData.json")
        mapData = json.load(mapData)
        
        y = 0
        for tile in mapData["Map"]["testMapData"]:
            x = 0
            for i in tile:
                x += 1
                if i == 1:
                    tile = pg.draw.rect(window, (255,255,255), (x * 20 , y * 20 , 20, 20))


                    if tile.colliderect(self.playerRect.x + self.dx, self.playerRect.y, 16,25):
                        self.dx = 0

                    if tile.colliderect(self.playerRect.x, self.playerRect.y + self.dy, 16,25):
                        self.dy = 0

                #print("a")

                if i == 0:
                    pg.Rect(x * 20, y * 20, 20, 20)
            y += 1


        self.x += self.dx
        self.y += self.dy 

    def Ai(self):
        pass
