https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2/stmpe-resistive-pinout

![[Pasted image 20250107165439.png]]
# Pinouts

There are three versions of the shield. One has a capacitive touch, the other two are the older and newer versions with resistive touch. The _TFT display_ and pinouts is the same for both. The microSD card is the same too. The differences come in on the touch screen controller and whether the SPI pins are connected to pins 11-13 or the ICSP header by default.

## TFT Screen Pins

- **Digital #13** _**or**_ **ICSP SCLK** - This is the hardware SPI clock pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #13. This pin is used for the TFT, microSD and resistive touch screen data clock
- **Digital #12** _**or**_ **ICSP MISO** - This is the hardware SPI Microcontroller In Serial Out pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #12. This pin is used for the TFT, microSD and resistive touch screen data
- **Digital #11** _**or**_ **ICSP MOSI** - This is the hardware SPI Microcontroller Out Serial In pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #11. This pin is used for the TFT, microSD and resistive touch screen data
- **Digital #10** - This is the TFT CS (chip select pin). It's used by the Arduino to tell the TFT that it wants to send/receive data from the TFT only
- **Digital #9** - This is the TFT DC (data/command select) pin. It's used by the Arduino to tell the TFT whether it wants to send data or commands

## Resistive Touch Controller Pins

- **Digital #13** _**or**_ **ICSP SCLK** - This is the hardware SPI clock pin. By default its on digital #13. By cutting a jumper and soldering another on the back, you can move this line from digital to the ICSP 2x3 header. This pin is used for the TFT, microSD and resistive touch screen data clock
- **Digital #12** _**or**_ **ICSP MISO** - This is the hardware SPI Microcontroller In Serial Out pin. By default its on digital #12. By cutting a jumper and soldering another on the back, you can move this line from digital to the ICSP 2x3 header. This pin is used for the TFT, microSD and resistive touch screen data
- **Digital #11** _**or**_ **ICSP MOSI** - This is the hardware SPI Microcontroller Out Serial In pin. By default its on digital #11.By cutting a jumper and soldering another on the back, you can move this line from digital to the ICSP 2x3 header. This pin is used for the TFT, microSD and resistive touch screen data
- **Digital #8** - This is the STMPE610 Resistive Touch CS (chip select pin). It's used by the Arduino to tell the Resistive controller that it wants to send/receive data from the STMPE610 only

## Capacitive Touch Pins

- **SDA** - This is the I2C data pin used by the FT6206 capacitive touch controller chip. It can be shared with other I2C devices. On UNO's this pin is also known as Analog 4.
- **SCL** - This is the I2C clock pin used by the FT6206 capacitive touch controller chip. It can be shared with other I2C devices. On UNO's this pin is also known as Analog 5.

## MicroSD card Pins

- **Digital #13** _**or**_ **ICSP SCLK** - This is the hardware SPI clock pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #13. This pin is used for the TFT, microSD and resistive touch screen data clock
- **Digital #12** _**or**_ **ICSP MISO** - This is the hardware SPI Microcontroller In Serial Out pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #12. This pin is used for the TFT, microSD and resistive touch screen data
- **Digital #11** _**or**_ **ICSP MOSI** - This is the hardware SPI Microcontroller Out Serial In pin. By default its on the 2x3 header. By cutting a jumper and soldering another on the back, you can move this line from ICSP to digital #11. This pin is used for the TFT, microSD and resistive touch screen data

- **Digital #4** - This is the uSD CS (chip select pin). It's used by the Arduino to tell the uSD that it wants to send/receive data from the uSD only