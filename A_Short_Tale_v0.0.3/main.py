#Main file for A Short Tale

class Game():
	
	def __init__(self):
		
		#Initialize game class, to hold variables for the user. This includes progress for saving, and other clever things John will think of. 
		
		
		self.chapter = 1
		self.prog = 0
		
		self.choices = {"Chapter1":{},
		   "Chapter2":{},
		   "Chapter3":{},
		   "Chapter4":{},
		   "Chapter5":{},
		   "Chapter6":{}}
				
game = Game()

from auxscripts.init import Hero

player = Hero("NONAME", "NOCLASS")

#Auxillary scripts6
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

player, story = main(player) #In MUSTFUNC, says new/load

game.chapter = int(story)
game.prog = story - game.chapter

chapter1(player)
