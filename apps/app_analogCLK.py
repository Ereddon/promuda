from promudaLib import LCD as lcd
from promudaLib import Buzzer as buz
from utime import sleep_us
import framebuf
import utime
import math
import ntptime
import network

# set the desired WIFI SSID and password here 
SSID ='20381'
PASSWORD ='pmd13533'

# set your timezone here
TZ = 7

# try to get clock from internet
net=network.WLAN(network.STA_IF)
try:
 lcd.text("Get time...",0,0,1)
 lcd.show()
 net.active(True)
 net.connect(SSID, PASSWORD)
 sleep_us(3000000)
 ntptime.settime()
except:
 lcd.fill(0)
 lcd.text("Failed!",0,0,1)
 lcd.show()
 net.active(False)

# frame buffer

FR_W = 96 
FR_H = 68
FR_OFFS_X = 0
FR_OFFS_Y = 0

SHAND_LEN = 30
MHAND_LEN = 25
HHAND_LEN = 20

sHand = framebuf.FrameBuffer(bytearray((FR_W * FR_H) // 8), FR_W, FR_H, framebuf.MONO_HLSB)
mHand = framebuf.FrameBuffer(bytearray((FR_W * FR_H) // 8), FR_W, FR_H, framebuf.MONO_HLSB)
hHand = framebuf.FrameBuffer(bytearray((FR_W * FR_H) // 8), FR_W, FR_H, framebuf.MONO_HLSB)
ctrX = (FR_W//2)
ctrY = (FR_H//2)

def getTick(tick, stretch, x1, y1):
    tick -= 15
    tick = tick % 60
    tick = 60 - tick
    x = math.cos(2 * math.pi * (tick / 60.0))
    y = -1 * math.sin(2 * math.pi * (tick / 60.0))
    x *= stretch
    y *= stretch
    x += x1
    y += y1
    return int(x), int(y)

sec = utime.localtime()[5]
while True:
 now = utime.localtime()
 if now[5]!=sec:
  sec = now[5]
  now_hour = (now[3]+(TZ)) % 12 
  now_minute = now[4]
  now_second = now[5]
  HOUR = getTick(((now_hour)*5)+(now_minute*5/60), HHAND_LEN, ctrX, ctrY)
  MIN = getTick(now_minute+(now_second/60.0), MHAND_LEN, ctrX, ctrY)
  SEC = getTick(now_second, SHAND_LEN, ctrX, ctrY)
  sHand.fill(0)
  mHand.fill(0)
  hHand.fill(0)
  lcd.fill(0)
  lcd.rect(FR_OFFS_X, FR_OFFS_Y, FR_W, FR_H, 1) 
  sHand.line(ctrX,ctrY,SEC[0],SEC[1],1)
  mHand.line(ctrX,ctrY,MIN[0],MIN[1],1)
  hHand.line(ctrX,ctrY,HOUR[0],HOUR[1],1)
  lcd.blit(sHand, 0, 0, 0)
  lcd.blit(mHand, 0, 0, 0)
  lcd.blit(hHand, 0, 0, 0)
  lcd.show()
  buz.tune(1,5)
 
