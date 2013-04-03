import spi
#initialize(mode, bitspermessage, speed, delay)
spi.initialize(0, 3, 400000, 3)

a = spi.transfer((1,2,3))
print a
a = spi.transfer((4,5,6))
print a
a = spi.transfer((7,8,9))
print a

spi.end()
