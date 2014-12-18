import unicornhat as UH
import time, colorsys
from random import randint
import urllib2

UH.brightness(0.3)

### Based on Code by @ben_Nuttal
def random_sparkle(): ### Code for a random LED if the letter value is below zero###
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        UH.set_pixel(x, y, r, g, b)
        UH.show()
        time.sleep(0.10)
        UH.clear()

website = urllib2.urlopen("enter address here")
##print website.read()

sentence = website.read()

print sentence

###Checks the letters in the sentence, then works out the co- ordinates###
for letter in sentence:
    index  = ord(letter)-65
    #print index ### remove when complete###
    if index > 0:
        x = int(index/8.0)
        #print x ### remove when complete###
        #x = x - 4
        y = int(index%8)
        #print (x, y)
        
        UH.clear
        UH.brightness(0.1)
        UH.set_pixel(y, x, 0, 255, 0)
        #UH.set_pixel(x, y, 0, 255, 0)
        UH.show()
        time.sleep(0.03)
        UH.clear()

    elif index <= 0:
        random_sparkle()
       
        

