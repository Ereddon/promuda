import·promudaCore
import·promudaLib
from·utime·import·sleep_us
 
#·the·demo·app·shown·all·Promuda's·board·basic·library·usage
 
#·display·text·parameter·-->·(the·text·,·display·line,·centered)
·
promudaCore.Display.printlcd('Hello·World!',1,True)
promudaCore.Display.printlcd('Welcome·to',2,True)
promudaCore.Display.printlcd('Promuda.',3,True)
promudaCore.Display.printlcd('Enjoy!',4,True)
 
#·button·enumeration·(this·should·be·built·in-library,·I·know..·my·bad)
 
A_BTN	=0b000001
B_BTN	=0b000010
UP		=0b000100
DOWN	=0b001000
LEFT	=0b010000
RIGHT	=0b100000
 
while·True:
··promudaLib.Button.getKey()
··#·get·which·key·is·pressed
··if·promudaLib.Button.keypressed·&·A_BTN:
····#·play·some·tune·on·buzzer!·parameter·-->·(the·notes,·duration·in·milliseconds)·
····promudaLib.Buzzer.tune(1,50)
····#·light·up·a·LED·parameter·-->·(which·LED)
····promudaLib.LED.on(0)
··if·promudaLib.Button.keypressed·&·B_BTN:
····promudaLib.Buzzer.tune(2,50)
····promudaLib.LED.on(1)
··if·promudaLib.Button.keypressed·&·UP:
····promudaLib.Buzzer.tune(3,50)
····promudaLib.LED.on(2)
··if·promudaLib.Button.keypressed·&·DOWN:
····promudaLib.Buzzer.tune(4,50)
····promudaLib.LED.on(0)
····promudaLib.LED.on(1)
··if·promudaLib.Button.keypressed·&·LEFT:
····promudaLib.Buzzer.tune(5,50)
····promudaLib.LED.on(0)
····promudaLib.LED.on(2)
··if·promudaLib.Button.keypressed·&·RIGHT:
····promudaLib.Buzzer.tune(6,50)
····promudaLib.LED.on(1)
····promudaLib.LED.on(2)
··if·promudaLib.Button.keypressed·==·0:
····#·turn·the·LED·off·if·no·keys·being·pressed
····for·i·in·range(3):
······promudaLib.LED.off(i)⇥⇥
··#·put·delay·a·bit·so·the·sound·appears·neat!
··sleep_us(500000)