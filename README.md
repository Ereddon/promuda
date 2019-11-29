![alt text](https://i.ibb.co/89XCHd2/seratuspersen.png)

# Promuda

![Front View](https://i.ibb.co/TvqhghP/promuda-front.png) 

Promuda is a wireless programmable electronic platform aiming for easy and simple embedded aplication development.

The main target audience for this board are everyone who has a mobile phone! No more bulky PC's needed. 

Promuda is designed to be able to programmed using a mobile phone out of the box. It has an application launcher and easy to use wifi manager. Just install a code editor and a downloader apk, and you are ready to go.

### Features

- All ESP8266 + Micropython features
- 4 Way directional button
- 2 Action button
- Buzzer
- 96x68 Monochrome display
- Promuda application launcher
- 8 Digital I/O (selectable through jumper)
- 1 ADC input (selectable through jumper)
- Rechargeable 1200mAh li-poly battery (so you can code on the go)

### Our recommended code editor for Android: 

[NotePad Pro](https://play.google.com/store/apps/details?id=com.exapps.notepad&hl=en)

It is the only text editor in playstore with whitespace marking option, which crucial when we works with python! Also no ads and no IAP.

### Application downloader 

Download it here [Promuda Programmer for Android](https://github.com/Ereddon/promuda/blob/master/tools/promuda_programmer_v103.apk)

## Getting Started

### Connecting to the board

1. Turn on your Promuda board
2. Go to Settings --> WIFI Info
3. Set your mobile phone SSID and Password
4. Turn on mobile hotspot 
5. Press the reset button on the Promuda board

### Write your first code

1. Open your favourite code editor on your mobile phone
2. Write your code! a simple hello world would be

```
import promudaCore

promudaCore.Display.printlcd('Hello World!',1,True)
```

3. "Save as" your file with this format: app_<your application name>.py

### Download your first code

1. On your Promuda board, check WIFI Menu. It should shows your board IP address
2. Open Promuda Programmer app
3. Edit the default IP address to follow your board IP address e.g change: 
```
ws://192.168.4.1:8266
```
to 
```
ws://192.168.43.8:8266 
```
4. Click "Choose File" and locate your first code file
5. Click "Send to device" and wait until it completed

### Run your first code

1. On your promuda board menu, go to "App"
2. It should shows your freshly written app name in the list
3. Select it --> Run
4. Your applicaton will run automatically after the board turned ON
5. To go back to Promuda menu, hold "A" button then press "RESET" button.

### Debug your code

If your promuda application caught an exception when running, the backlight will be blinked continuously. Then we need to find out why by debug it.

Oh, we can do that?

Unfortunately there is no debug feature, yet. But you can see the last error/exception from your code by clicking "Get last error" button in the android app.

### Force boot to Promuda menu

Hold "A" button while your Promuda board booted up.

### Repair bricked devices

Although this is rare, but your devices can be bricked. Too many write process to the filesystem will ramp up the risk! To make it minimum to none, avoid any "write to file" process in your application. The recovery process is TBD.

