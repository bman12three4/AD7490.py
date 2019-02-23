# AD7490.py
Python driver for the Analog Devices AD7490 16 channel 12 bit ADC using the Adafruit FT232H breakout board.

# How to install
This code uses the Adafruit_GPIO library to comminicate with the FT232H. Download that [here](https://github.com/adafruit/Adafruit_Python_GPIO/archive/master.zip)

Make sure you also install the appropriate drivers from FTDI which you can find the links to on Adafruit's website [here](https://learn.adafruit.com/adafruit-ft232h-breakout/mpsse-setup)

# How to use
import the code with `import AD7490`, then create the object with `obj = AD7490.adc()`
