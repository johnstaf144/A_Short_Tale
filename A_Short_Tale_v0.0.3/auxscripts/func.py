from colorama import Fore
import os
import time
import sys

#Auxillary scripts
from auxscripts.fullscreen import * #To go full screen
from auxscripts.init import * #Initialise game
from auxscripts.MUSTFUNC import * #VERY IMPORT FUNCTIONS TO THE STORY
from auxscripts.func import * #Useful functions
from auxscripts.values import * #Values

#Save
from auxscripts.save import *

def jinput(string):
	"""
	New input so player can quit whenever he likes.
	"""
	ans = input(Fore.CYAN + string + Fore.GREEN).lower()
	if ans == "y":
		ans = "yes"
	elif ans == "n":
		ans = "no"
	if ans.lower() in l_quit:
		quit() # Add saving later
	elif ans.lower() == "save":
		save_progress()
	else:
		return ans

def jinputUpper(string):
	"""
	New input so player can quit whenever he likes.
	"""
	ans = input(Fore.CYAN + string + Fore.GREEN)
	if ans.lower() in l_quit:
		quit() # Add saving later
	else:
		return ans
	
def quit():
	print("Thank you for playing!")
	time.sleep(2)
	sys.exit()
		
clear = lambda: os.system('cls')