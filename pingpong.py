from pygame import *
from time import sleep


bg_color = (255,255,255)
window = display.set_mode((600,500))
display.set_caption('Ping Pong')
#window.fill(bg_color)


background = transform.scale(image.load('background.png'),(600,500))
fps = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,width,height,img,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width,height))
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'right'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >100:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 410 - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >100:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 410 - 80:
            self.rect.y += self.speed



p1 = Player1(65,65,'shield.png',414,210,10)
p2 = Player2(65,65,'shield.png',119,210,10)
ball = Player2(30,30,'bola.png',168,210,5)

speed_x = ball.speed
speed_y = ball.speed

game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    p1.reset()
    p1.update()
    p2.reset()
    p2.update()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    ball.update()
    display.update()

    if ball.rect.y > 410-80 or ball.rect.y <100:
        speed_y *= -1

    if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
        speed_x *= -1
    
    if ball.rect.x >= 700:
        font.init()
        font1 = font.Font(None,35)
        youlose= font1.render('PLAYER 2 LOSE',True,(0,180,0))
        window.blit(youlose,(600/2,500/2))

    fps.tick(60)