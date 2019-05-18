from colorama import Fore
import os
import time
import sys

from auxscripts.values import l_quit #Values
from auxscripts.init import player #Values

#Save
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
		#print(player.name)
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

def save_progress():
	
	player_atts = [player.name,
			player.inventory,
			player.Class,
	
			player.mage,
			player.warrior,
			player.berserker,
			player.assassin,
			player.yeet,
			player.hidden_class,
			
			#player stats
			player.speed,
			player.perception,
			player.magic,
			player.strength,
			player.stealth,
			player.speech,
			player.constitution,
			
			#player skills for chapter 1
			player.pickpocket,
			player.lock_pick,
			player.self_combust,
			player.hold_breath,
			player.animal_lang,
			player.premonition,
			player.apocalypse]
	
	
	save_file = open("save.txt", "w")
	
	save_file.write("#PLAYER\n")
	for stat in player_atts:
		save_file.write(str(stat))
		save_file.write("\n")
		
	save_file.write("#STORY\n")
	save_file.write("4.12\n")
					
	save_file.write("#CHOICES\n")
	save_file.write("{Chaper}")
		
	save_file.close()
	
	print("Saved progress!")
	time.sleep(1)