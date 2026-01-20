from pygame import *

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



    fps.tick(60)
    display.update()