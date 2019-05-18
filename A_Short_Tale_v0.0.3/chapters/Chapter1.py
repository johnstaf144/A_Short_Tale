############################################################
##############CHAPTER 1#####################################
############################################################
#dream, you choose to do one of four options which will result in either carrying on as normal
#or storing the hidden class variable if you know the specific answer!
import time
from auxscripts.init import player #Initialise game
from auxscripts.values import choices

#Functions
from chapters.Chapter1Func import player_name, dream, take_hand

def chapter1(prog):
					
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
				
		#Get player name and create class
		p_name = player_name()
		player.name = p_name
		print("I MADE THE FUCKING HERO, HIS NAME IS {}".format(player.name))
				
		#Choice
		choice = take_hand()
		choices["Chapter1"].update({"Take Hand":choice})
		if not choice:
			print("\nYou really should have taken his hand... He stabs you and walks away whistling a merry tune.")
			
		
	
