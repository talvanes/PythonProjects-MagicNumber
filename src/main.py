# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from random import random

__author__ = "talba"
__date__ = "$19/04/2015 18:14:06$"

if __name__ == "__main__":
  '''
    I want a number from 0 to 100, so let's call it...
  '''
  magicNumber = int(100 * random())
  
  for i in range(101):
    if i is magicNumber:
      print(i, "is the magic number!")
      break
    elif i % 4 == 0:
      print(i)
