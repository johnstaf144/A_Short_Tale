#Main file for A Short Tale

#Auxillary scripts
from auxscripts.fullscreen import AltENTER #To go full screen
from auxscripts.MUSTFUNC import art, kart, main #VERY IMPORT FUNCTIONS TO THE STORY

import os

#Chapters
from chapters.Chapter1 import chapter1

clear = lambda: os.system('cls')

AltENTER() #Make full screen.
		  
kart() #Animation
clear() #Clear cmd 
art() #Create menu art
      
story = main() #In MUSTFUNC, says new/load

chapter = int(story)
prog = story - chapter

chapter1(prog)
