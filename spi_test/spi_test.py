import spidev

DEBUG = 0

spi = spidev.SpiDev()

#opens object in 0,0:
spi.open(0,0)

