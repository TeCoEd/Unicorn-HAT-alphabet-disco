import unicornhat as UH
import time, colorsys
from random import randint
import urllib2

### Random Sparkles Based on Code by @ben_Nuttal###
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

def option_1():###User enters a sentance to create the light show###
      
        phrase = raw_input("Please enter your phrase ").lower()

        ###Checks the letters in the phrase, then works out the co- ordinates###
        for letter in phrase:
            index  = ord(letter)-65
            #print index ### remove when complete###
            if index > 0:
                x = int(index/8.0)
                #print x ### remove when complete###
                x = x - 4
                y = int(index%8)
                #print (x, y)
                
                UH.clear
                UH.brightness(0.20)
                UH.set_pixel(y, x, 255, 255, 255)
                #UH.set_pixel(x, y, 0, 255, 0)
                UH.show()
                time.sleep(0.5)
                UH.clear()

            elif index <= 0:
                random_sparkle()        

def option_2():###Select a website to create the light show
        your_webiste_choice = raw_input("Please enter the web address")
        final_address = "http://%s" %(your_webiste_choice)
        print "finding", final_address 
        website = urllib2.urlopen(final_address )
        ##print website.read()

        sentence = website.read()

        print sentence
        
        ###Checks the letters in the website, then works out the co- ordinates###
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
                UH.brightness(0.2)
                UH.set_pixel(y, x, 0, 255, 0)
                UH.set_pixel(x, y, 0, 255, 0)
                UH.show()
                time.sleep(0.02)
                UH.clear()

            elif index <= 0:
                random_sparkle()

def start_code():
    global Program_Running 
    Program_Running = 1
    while Program_Running > 0:
            
        print""
        
        choice = raw_input("Please enter your selection ").lower()
        print""
        if choice == "1":
            option_1()
        if choice == "2":
            print "Please remove the letter sheet"
            print""
            time.sleep(1)
            option_2()
        if choice =="x":
            print "Bye Bye"
            Program_Running = 0
        #else:
            #print "Invalid selection"                

global Program_Running

print "Welcome to the Alphabet Light Show"
time.sleep(1)
print""
print "Please Make a Selection"
print""
time.sleep(1)
print "Press 1 to type in your own phrase"
time.sleep(2)
print ""
print "Press 2 to see what a website code looks like as a light show!"
time.sleep(1)
print""
print "Press X to quit"

start_code()            
        
        
    

       

