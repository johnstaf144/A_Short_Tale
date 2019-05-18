############################################################
##############CHAPTER 1#####################################
############################################################
#dream, you choose to do one of four options which will result in either carrying on as normal
#or storing the hidden class variable if you know the specific answer!
import os
import ctypes.wintypes as wintypes
from colorama import Fore
import ctypes
import msvcrt
import subprocess
import time
import win32com.client as comclt

#Auxillary scripts
from auxscripts.fullscreen import * #To go full screen
from auxscripts.init import * #Initialise game
from auxscripts.MUSTFUNC import * #VERY IMPORT FUNCTIONS TO THE STORY
from auxscripts.func import * #Useful functions
from auxscripts.values import * #Values

#Functions
from chapters.Chapter1Func import *
from auxscripts.save import *

def chapter1(prog):
	
	Class = "NOTCHOSEN"
	p_name = "NOTCHOSEN"	
	
	global player
	player = Hero(p_name, Class)
	
	print(player.name)
	
	if prog <= 0:
		#Dream
		print("You find yourself wandering a forest, a dream")
		dream()
	
	if prog <= 0.1:
	
		#Awake
		print("""\nYou wake up to the sounds of birds chirping in the trees around you. Slowly, as your blurry 
	vision begins to focus you realise a small boy is standing over you, a wide grin on his face.""")
		time.sleep(1)
		print("""\nBefore you have a chance to get up he sticks out his hand, asking you a question in a cheery voice,
	\"What's your name mister?\"""")
		
		#Get player name
		p_name = player_name()
		player.name = p_name
		
		#Choice
		choice = take_hand()
		choices["Chapter1"].update({"Take Hand":choice})
		if not choice:
			print("\nYou really should have taken his hand... He stabs you and walks away whistling a merry tune.")
	
