from colorama import Fore
import os
import time
import sys

from auxscripts.values import l_quit #Values
from __main__ import game, player

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
	elif "save" in ans.lower():
		split_save = ans.lower().split(" ")
		name = " ".join(split_save[1:])
		if name == "":
			save_progress()
		else:
			save_progress(name)
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

def save_progress(name = "AutoSave"):
	
	name = name + ".txt"
	
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
	
	path_to_dir = os.path.abspath(".")
	save_file = open(path_to_dir + "/saveData/{}".format(name), "w")
	
	save_file.write("#PLAYER\n")
	for stat in player_atts:
		save_file.write(str(stat))
		save_file.write("\n")
		
	save_file.write("#STORY\n")
	save_file.write(str(game.prog))
	save_file.write("\n")
					
	save_file.write("#CHOICES\n")
	save_file.write(str(game.choices))
		
	save_file.close()
	
	print("Saved progress!")
	time.sleep(1)
	
def update_prog(amount = 0.01):
	game.prog += amount 
	
def tolist(l):
	return l[1:-1].split(",") #removes square brackets, and splits by comma, resulting in list

def recap(chap):
	print(Fore.GREEN + "Here is a recap of your story so far, now that you have finished Chapter {}.".format(chap))
	print("Your story progress number is {}.\n".format(game.prog))
	print("In your inventory, you currently have:")
	for item in player.inventory:
		print("    -{}".format(item))
	print("\n")
	print("The choices you have made are: ")
	for choice in game.choices["Chapter{}".format(chap)]:
		print("For the {} choice, you chose {}.".format(choice, game.choices["Chapter{}".format(chap)][choice]))
		