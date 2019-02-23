import time
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H
import struct


class adc():
    def __init__(self):


        '''This code is taken from the SPI example on Adafruit's Website
           https://learn.adafruit.com/adafruit-ft232h-breakout/spi
        '''

        # Temporarily disable FTDI serial drivers.
        FT232H.use_FT232H()
        # Find the first FT232H device.
        ft232h = FT232H.FT232H()
        # Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
        # Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
        self.spi = FT232H.SPI(
            ft232h, cs=8, max_speed_hz=3000000, mode=0, bitorder=FT232H.MSBFIRST)
		
		self.power_mode = 3 	# set power mode to normal
		self.dout = 0			# set DOUT to three state at end of transfer
		self.range = 0			# set range to double Vref
		self.coding = 1			# set coding to straight binary
		self.seq = 0			# turn off sequencer
		self.write = 1			# write command 
		self.shadow = 0			# turn off sequencer

        # Initialize ADC after  power up by sending ones for two cycles.
        self.spi.write([0xff, 0xff])
        self.spi.write([0xff, 0xff])



    def readAll(self):
        return self.read(16)

    def readChannels(self, channels):
        values = range(channels)
        for x in values:
            values[x] = self.readChannel(x)
        
        return values

    def readChannel(self, channel):
        #Basic data word, sets power functions to normal, goes to address 0, range is 2x
        byte1 = 0x00 | (write << 7) | (seq << 6) | (channel << 2) | (self.power_mode)
        byte2 = 0x00 | (shadow << 7) |(self.dout << 6) | (self.range << 5) | (self.coding << 4)

        self.spi.write([byte1, byte2])

        ret = self.spi.read(2)
        response = struct.unpack('>H', ret)[0] & 4095

        return response
		
	def setSeq(self, mode):
		self.seq = mode
		
	def setShadow(self, mode):
		self.shadow = mode
		
	def setPowerMode(self, mode):
		self.power_mode = mode
		
	def setDOUT(self, mode):
		self.dout = mode
		
	def setRange(self, mode):
		self.range = mode
	
	def setCoding(self, mode):
		self.coding = mode
