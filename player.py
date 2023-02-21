
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
        self.bulletSpeed = 7
        self.bulX = self.x
        self.bulY = self.y


    def playerEvent(self, pg, window):
        self.keyinput = pg.key.get_pressed()
        self.playerRect = pg.Rect(self.x , self.y, 16,25)
        pg.draw.rect(window, (255,255,255), (self.playerRect))
        

        #MOVEMENT
        if self.keyinput[pg.K_a]:
            self.x -= self.pSpeed

        if self.keyinput[pg.K_d]:
            self.x += self.pSpeed


        if self.keyinput[pg.K_w]:
            self.y -= self.pSpeed

        if self.keyinput[pg.K_s]:
            self.y += self.pSpeed




    def playerGun(self, pg, window, config):
        fire = pg.mouse.get_pressed()[0] 
        mx,my = pg.mouse.get_pos()
        mx // config["Display"]["dynamicRes"]
        my // config["Display"]["dynamicRes"]


        pg.draw.line(window, (30,200,30), (mx// config["Display"]["dynamicRes"], my// config["Display"]["dynamicRes"]),(self.x + 8, self.y))
        pg.draw.circle(window, (200,30,30), (mx// config["Display"]["dynamicRes"], my// config["Display"]["dynamicRes"]), 2)


        if fire:
            self.bullet.append([pg.image.load("data/bulSprite.png") ,  self.x + 8, self.y,
            mx // config["Display"]["dynamicRes"],
            my // config["Display"]["dynamicRes"],
            math.atan2(self.y - my // config["Display"]["dynamicRes"], self.x - mx // config["Display"]["dynamicRes"]),
            
            ])


        for bullet in self.bullet:
            bulletRect = bullet[0].get_rect()

            xVel = math.cos(bullet[5]) * self.bulletSpeed
            yVel = math.sin(bullet[5]) * self.bulletSpeed
            
            window.blit(bullet[0], (bullet[1] , bullet[2]))
            bullet[1] -= xVel
            bullet[2] -= yVel



    def gameMap(self):
        pass