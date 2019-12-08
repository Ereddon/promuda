from promudaLib import LCD as lcd
from promudaLib import Buzzer as buz
from promudaLib import LED as led
from promudaLib import Button as btn

from utime import sleep_us

# the demo app shown all Promuda's board basic library usage

# display text parameter --> (the text , display line, centered)
 
lcd.text('Hello World!',1,1,1)
lcd.text('Welcome to',1,12,1)
lcd.text('Promuda.',1,24,1)
lcd.text('Enjoy!',1,36,1)
lcd.show()

# button enumeration (this should be built in-library, I know.. my bad)

A_BTN	=0b000001
B_BTN	=0b000010
UP		=0b000100
DOWN	=0b001000
LEFT	=0b010000
RIGHT	=0b100000

while True:
  btn.getKey()
  # get which key is pressed
  if btn.keypressed & A_BTN:
    # play some tune on buzzer! parameter --> (the notes, duration in milliseconds) 
    buz.tune(1,50)
    # light up a LED parameter --> (which LED)
    led.on(0)
  if btn.keypressed & B_BTN:
    buz.tune(2,50)
    led.on(1)
  if btn.keypressed & UP:
    buz.tune(3,50)
    led.on(2)
  if btn.keypressed & DOWN:
    buz.tune(4,50)
    led.on(0)
    led.on(1)
  if btn.keypressed & LEFT:
    buz.tune(5,50)
    led.on(0)
    led.on(2)
  if btn.keypressed & RIGHT:
    buz.tune(6,50)
    led.on(1)
    led.on(2)
  if btn.keypressed == 0:
    # turn the LED off if no keys being pressed
    for i in range(3):
      led.off(i)
  # put delay a bit so the sound appears neat!
  sleep_us(500000)