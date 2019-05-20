############################################################
##############CHAPTER 1#####################################
############################################################
#dream, you choose to do one of four options which will result in either carrying on as normal
#or storing the hidden class variable if you know the specific answer!
from colorama import Fore

import time
from auxscripts.func import update_prog, recap, save_progress
from __main__ import game, player

#Functions
from chapters.Chapter1Func import player_name, dream, take_hand

def chapter1(player):
						
	if game.prog <= 0:
		#Dream
		print("You find yourself wandering a forest, a dream")
	
		dream_choice = game.make_choice("Run or stay", "Do you?", "Run", "Stay", secret = ["Wake up"])
		if dream_choice == "A":
			print("You run")
		elif dream_choice == "B":
			print("You stay")
		elif dream_choice == "WAKE UP":
			print("You realise")
		update_prog()
		
	if game.prog <= 0.01:
	
		#Awake
		print("""\nYou wake up to the sounds of birds chirping in the trees around you. Slowly, as your blurry 
	vision begins to focus you realise a small boy is standing over you, a wide grin on his face.""")
		time.sleep(1)
		print("""\nBefore you have a chance to get up he sticks out his hand, asking you a question in a cheery voice,
	\"What's your name mister?\"""")
				
		#Get player name and create class
		p_name = player_name()
		player.name = p_name
			
		choice = game.make_choice("Take hand", "Do you take his hand?", "Yes", "No")
        if choice == "A":
            pickup("Hand")
		if choice == "B":
			print(Fore.GREEN + "\nYou really should have taken his hand... He stabs you and walks away whistling a merry tune.")
			
		update_prog()
		
	if game.prog <= 0.02:
		
		print(Fore.GREEN + "Get fucked {}".format(player.name))
	
	print("\n")	
	print(Fore.CYAN + "Chapter finished")
	recap(1)
	
	game.chapter = 2
	game.prog = 0
	save_progress(quiet = True)
	
	input("Press any key to finish")
