from pygame import *

bg_color = (50,100,23)
window = display.set_mode((600,500))
display.set_caption('Ping Pong')
window.fill(bg_color)

fps = time.Clock()

game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    #window.blit(background,(0,0))
    fps.tick(60)
    display.update()