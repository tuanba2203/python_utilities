#!/bin/python3
'''
Author: TuanBA
`recursiveExponentCidr()` function uses recursive to calcuate the exponent of CIDR with provided CIDR Block Size. 
Usage: change value of `CIDRSize` variable to the CIDR Block size that you want.
e.g. 
with CIDRSize = 128, your CIDR block must be something like a.b.c.d/25
'''


## Do recursive to find Exponent of Cidr 
def recursiveExponentCidr(input):
  global exponentCounter
  exponentCounter += 1
  if input <= 2:
    return 1
  else:
    res = recursiveExponentCidr(input/2)
    return res

CIDRSize = 128
exponentCounter = int(0)
recursiveExponentCidr(CIDRSize)
possibleSubnetMask = 32 - exponentCounter
print('CIDR a.b.c.d/' + str(possibleSubnetMask))
