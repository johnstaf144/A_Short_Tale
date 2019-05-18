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
	dream_choice_1 = jinput("Do you: \nA: Run \nB: stay \n")
	if dream_choice_1 == "a":
		pass
	elif dream_choice_1 == "b":
		jinput("000") ##DO SOMETHING
	elif dream_choice_1 == "wake up":
		global hidden_class
		hidden_class += 1
		print("\nYou realise")
	else:
		print(required)
		dream()

def player_name():
	p_name = jinputUpper("\n" + Fore.CYAN + "Choose a name: " + Fore.GREEN)
	certain = jinput("\n" + Fore.CYAN + "Are you sure?: " + Fore.GREEN)
	if certain == "yes":
		print ("\n\"Well, hi " + p_name + "! My name is Iri! Saw ya lying over and thought it best not to wake ya!... Want a hand up?\"")
		return p_name
	elif certain in no:
		player_name()
	else:
		print(required)
		player_name()

#decision to take the boy's hand
def take_hand():
	hand = jinput("\n" + Fore.CYAN + "Do you take his hand?: " + Fore.GREEN)
	if hand == "yes":
		print(Fore.GREEN + "\nI love you!!!")
		return True
	elif hand == "no":
		return False
	else:
		print(required)
		take_hand()

#main()
#quit()

