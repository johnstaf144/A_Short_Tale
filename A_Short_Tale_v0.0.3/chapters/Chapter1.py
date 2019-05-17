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

def dream():
	print("You find yourself wandering a forest, a dream")
	dream_choice_1 = jinput("Do you: \nA: Run \nB: stay \n")
	if dream_choice_1 in answer_A:
		awake()
	elif dream_choice_1 in answer_B:
		jinput("000")
	elif dream_choice_1 == "wake up":
		global hidden_class
		hidden_class += 1
		print("")
		print("You realise")
		awake()
	else:
		print(required)
		dream()


def awake():
	print(" ")
	print("""You wake up to the sounds of birds chirping in the trees around you. Slowly, as your blurry
vision begins to focus you realise a small boy is standing over you, a wide grin on his face.""")
	time.sleep(1)
	print(""" 
Before you have a chance to get up he sticks out his hand, asking you a question in a cheery voice,
\"What's your name mister?\"""")
	player_name()
	

def player_name():
	global p_name
	print("")
	p_name = jinput(Fore.CYAN + "Choose a name: " + Fore.GREEN)
	print(" ")
	certain = jinput(Fore.CYAN + "Are you sure?: " + Fore.GREEN)
	if certain in yes:
		print(" ")
		print ("\"Well, hi " + p_name + "! My name is Iri! Saw ya lying over and thought it best not to wake ya!... Want a hand up?\"")
		choice_1()
	elif certain in no:
		player_name()
	else:
		print(required)
		player_name()

#decision to take the boy's hand
def choice_1():
	print(" ")
	hand = jinput(Fore.CYAN + "Do you take his hand?: " + Fore.GREEN)
	if hand in yes:
		hand_yes()
	elif  hand in no:
		hand_no()
	else:
		print(required)
		choice_1()

def hand_yes():
	print(" ")
	print("I love you!!!")
	quit()

def hand_no():
	global constitution
	print("")
	print("You really should have taken his hand... He stabs you and walks away whistling a merry tune.")
	death = jinput ("You died, would you like to start again... or get up!?: ")
	if death in yes:
		pass
		#main()
	elif death in no:
		exit()
	elif death == "NOOO" or death == "get up" or death == "NO" or death == "stand up":
		strength
		constitution += 2 
		hardy()

def hardy():
	global yes
	print("YOU'RE ALIVE")

#main()
#quit()

