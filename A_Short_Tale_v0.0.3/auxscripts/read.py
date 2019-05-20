#from auxscripts.init import Hero
import auxscripts.init
import os
from auxscripts.func import tolist
from ast import literal_eval

def load():
	
	path_to_dir = os.path.abspath(".")
	save_file = open(path_to_dir + "/saveData/save.txt", "r")
	#save_file = open("../saveData/save.txt", "r") #For debugging, reads file but you can run the function from this script.
	read_file = save_file.read().split("\n")
	save_file.close()
	
	player_index = 0
	story_index = read_file.index("#STORY")
	choice_index = read_file.index("#CHOICES")
								   
	player_atts = read_file[player_index + 1:story_index]
	story_progress = float(read_file[story_index + 1])
	choices = read_file[choice_index + 1]
	
	#%% Recreate player
	player = auxscripts.init.Hero(player_atts[0], player_atts[2])
		
	player.mage = player_atts[3]
	player.warrior = player_atts[4]
	player.berserker = player_atts[5]
	player.assassin = player_atts[6]
	player.yeet = player_atts[7]
	player.hidden_class = player_atts[8]
	
	#player stats
	player.speed = player_atts[9]
	player.perception = player_atts[10]
	player.magic = player_atts[11]
	player.strength = player_atts[12]
	player.stealth = player_atts[13]
	player.speech = player_atts[14]
	player.constitution = player_atts[15]
	
	#player skills for chapter 1
	player.pickpocket = player_atts[16]
	player.lock_pick = player_atts[17]
	player.self_combust = player_atts[18]
	player.hold_breath = player_atts[19]
	player.animal_lang = player_atts[20]
	player.premonition = player_atts[21]
	player.apocalypse = player_atts[22]

	
	#%% Recreate Inventory

	player.inventory = tolist(player_atts[1])
	
	#%% Recreate Choices
	
	choices = literal_eval(choices)
	
	return player, story_progress, choices