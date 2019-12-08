from promudaLib import LCD as lcd
from promudaLib import Buzzer as buz
from promudaLib import Button as btn
from utime import sleep_us
import framebuf
import time

SCREEN_WIDTH = 96
SCREEN_HEIGHT = 68

game_over = False
score = 0

class Entity:
    def __init__(self, x, y, w, h, vx, vy):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.vx = vx;
        self.vy = vy;

    def draw(self, lcd):
        lcd.fill_rect(int(self.x), int(self.y), self.w, self.h, 1)

class Ball(Entity):
    def update(self, dt, player):
        self.x += self.vx * dt;
        if (self.x <= 0):
            self.x = 0
            self.vx = -self.vx
            buz.tune(2,20)
        if (self.x >= SCREEN_WIDTH - self.w):
            self.x = SCREEN_WIDTH - self.w
            self.vx = -self.vx
            buz.tune(2,20)
        self.y += self.vy * dt;
        if (self.y <= 0):
            self.y = 0
            self.vy = -self.vy
            buz.tune(2,20)
        if (self.y >= SCREEN_HEIGHT - self.h - player.h):
            if (self.x >= player.x and self.x <= player.x + player.w):
                self.y = SCREEN_HEIGHT - self.h - player.h
                self.vy = -self.vy
                global score
                score += 1
                buz.tune(1,20)
                if score % 2 == 0:
                    self.vx += (self.vx/abs(self.vx)) * 1
                if score % 3 == 0:
                    self.vy += (self.vy/abs(self.vy)) * 1
            else:
                global game_over
                game_over = True

class Player(Entity):
    pass

ball = Ball(32, 16, 4, 4, 2, -2)
player = Player(40, 66, 25, 2, 0, 0)
fbuf = framebuf.FrameBuffer(bytearray(SCREEN_WIDTH * SCREEN_HEIGHT // 8), SCREEN_WIDTH, SCREEN_HEIGHT, framebuf.MONO_HLSB)
tick = time.ticks_ms()

LEFT = 0b010000
RIGHT = 0b100000

while not game_over:
    btn.getKey()
    ntick = time.ticks_ms()
    ball.update(time.ticks_diff(ntick, tick) // 100, player)
    tick = ntick
    if(btn.keypressed & LEFT):
     player.x=player.x-2
     player.x=0 if player.x<=0 else player.x-2 
    if(btn.keypressed & RIGHT):
     player.x=player.x+2
     player.x=71 if player.x>=71 else player.x+2
    fbuf.fill(0)
    ball.draw(fbuf)
    player.draw(fbuf)
    lcd.fill(0)
    lcd.blit(fbuf, 0, 0, 0)
    lcd.show()
    sleep_us(50000)

fbuf.fill(0)
fbuf.text('SCORE:'+str(score), 20, 22)
buz.tune(3,50)
buz.tune(8,100)
lcd.fill(0)
lcd.blit(fbuf, 0, 0, 0)
lcd.show()
sleep_us(2000000)
fbuf.fill(0)
fbuf.text('GAME', 30, 24)
fbuf.text('OVER', 30, 36)
lcd.fill(0)
lcd.blit(fbuf, 0, 0, 0)
lcd.show()
buz.tune(3,100)
buz.tune(2,100)
buz.tune(1,100)
