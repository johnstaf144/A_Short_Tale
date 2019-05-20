#Main file for A Short Tale

from colorama import Fore
from auxscripts.save import save_progress
import sys, time

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
		
	def make_choice(self, name, question ,*args, secret = []):
		secret = [i.upper() for i in secret]
		print(Fore.CYAN + question)	
		for j, i in enumerate(args):
			print(Fore.GREEN + "{}: {}".format(chr(65 + j), i))
		ans = input("").upper()
		if "save" in ans.lower():
			split_save = ans.lower().split(" ")
			name = " ".join(split_save[1:])
			if name == "":
				save_progress()
			else:
				save_progress(name)		
		if ans in secret:
			self.choices["Chapter1"].update({name:ans})
			return ans
		if ans == "QUIT":
			quit()
		while ans not in [chr(65 + i) for i in range(len(args))]:	
			if "save" not in ans.lower():
				print(Fore.RED + "Please enter a valid response!")
			print(Fore.CYAN + question)
			for j, i in enumerate(args):
				print(Fore.GREEN + "{}: {}".format(chr(65 + j), i))	
			ans = input("").upper()	
			if "save" in ans.lower():
				split_save = ans.lower().split(" ")
				name = " ".join(split_save[1:])
				if name == "":
					save_progress()
				else:
					save_progress(name)		
			if ans in secret:
				self.choices["Chapter1"].update({name:ans})
				return ans
			if ans == "QUIT":
				quit()
		self.choices["Chapter1"].update({name:args[ord(ans) - 65]})
		return ans

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

def quit():
	print("Thank you for playing!")
	time.sleep(2)
	sys.exit()

AltENTER() #Make full screen.
		  
kart() #Animation
clear() #Clear cmd 
art() #Create menu art

player, story = main(player) #In MUSTFUNC, says new/load

game.chapter = int(story)
game.prog = story - game.chapter

chapter1(player)
