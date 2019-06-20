############################################################
##############CHAPTER 1#####################################
############################################################
#dream, you choose to do one of four options which will result in either carrying on as normal
#or storing the hidden class variable if you know the specific answer!
from colorama import Fore

import time, sys, random
from auxscripts.func import update_prog, recap, save_progress
from __main__ import game, player

#Functions
from chapters.Chapter1Func import player_name, dream, take_hand

def pprint(s):
	print(s)

def chapter1(player):
						
	if game.prog <= 0:
		#Dream
		pprint("You find yourself wandering a forest, a dream.\n")
	
		dream_choice = game.make_choice("Run or stay", "Do you?", "Run", "Stay", secret = ["Wake up"])
		if dream_choice == "A":
			pprint("You run.\n")
		elif dream_choice == "B":
			pprint("You stay.\n")
		elif dream_choice == "WAKE UP":
			pprint("You realise...\n")
			
		time.sleep(1)
		
		update_prog()
		
	if game.prog <= 0.01:
	
		#Awake
		pprint("You wake up to the sounds of birds chirping in the trees around you. Slowly, as your blurry vision begins to focus you realise a small boy is standing over you, a wide grin on his face.\n")
		time.sleep(1)
		pprint("Before you have a chance to get up he sticks out his hand, asking you a question in a cheery voice.\n")
		time.sleep(1)
		pprint("\"What's your name mister?\"\n")
				
		#Get player name and create class
		p_name = player_name()
		player.name = p_name
		
		update_prog()
		
	if game.prog <= 0.02:
					
		choice = game.make_choice("Take hand", "Do you take his hand?", "Yes", "No")
		if choice == "A":
			player.pickup("Hand")
			time.sleep(1)
		if choice == "B":
			pprint(Fore.GREEN + "You really should have taken his hand... He stabs you and walks away whistling a merry tune.")
			time.sleep(1)
			
		update_prog()
		
	if game.prog <= 0.03:
		
		print(Fore.GREEN + "Get fucked {}".format(player.name))
	
	print("\n")	
	print(Fore.CYAN + "Chapter finished!\n")
	recap(player, 1)
	
	game.chapter = 2
	game.prog = 0
	save_progress(quiet = True)
	
	input("Press any key to finish")
