import spi
import time

#initialize(mode, bitspermessage, speed, delay)



#Define some constants
READ = 0b00000011
WRITE = 0b00000010
LOOPBACK = 0b01000000
CANSTAT = 0b00001110


def spi_send(message):



spi.initialize(0, 2, 500000, 0)
a = spi.transfer((WRITE, LOOPBACK))
for bit in a:
    print bin(bit)

spi.initialize(0, 3, 500000, 0)
a = spi.transfer((READ,CANSTAT,0))

for bit in a:
    print bin(bit)

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
