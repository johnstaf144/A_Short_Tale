from __main__ import *
import time

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