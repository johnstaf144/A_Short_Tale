from __main__ import game, player
from datetime import datetime

def save_progress(name = "AutoSave", quiet = False):
	
	if name == "AutoSave":
		name = name + datetime.now().strftime("at %H.%M on %d-%m")
	
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
	
	if not quiet:
		print("Saved progress!")
	time.sleep(1)