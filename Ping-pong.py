from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and  self.rect.y < width - 50:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and  self.rect.y < width - 50:
            self.rect.y += self.speed

width = 700
height = 500
window = display.set_mode((width,height))
display.set_caption("Пинг-понг")
background = (200, 255, 255)
window.fill(background)
count = 0
game = True
finish = False
FPS = 60
clock = time.Clock()

font1 = font.SysFont("Arial",36)
lose1 = font1.render('Игрок1 проиграл!', True, (255, 0, 0))
lose2 = font1.render('Игрок2 проиграл!', True, (255, 0, 0))
