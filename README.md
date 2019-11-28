![alt text](https://i.ibb.co/89XCHd2/seratuspersen.png)

# Promuda

Promuda is a wireless programmable electronic platform aiming for easy and simple embedded aplication development.

The main target audience for this board are everyone who has a mobile phone!

Promuda is designed to be able to programmed using a mobile phone. Just install a code editor and downloader app, and you are ready to go.

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
