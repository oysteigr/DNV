import spi
import time

#initialize(mode, bitspermessage, speed, delay)

spi.initialize(0, 1, 500000, 0)
a = spi.transfer((192,))
print a
