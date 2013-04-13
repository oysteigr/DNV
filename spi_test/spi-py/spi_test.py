import spi
import time

#initialize(mode, bitspermessage, speed, delay)

spi.initialize(0, 3, 500000, 0)
a = spi.transfer((3,14,0))
print a
#a = spi.transfer((192))
#
#print a
#a = spi.transfer((192,1,1))
#print a
#spi.initialize(0, 4, 500000, 0)
#a = spi.transfer((4,5,6,192))
#print a
#a = spi.transfer((7,8,9))
#print a

spi.end()
