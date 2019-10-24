#Main file for A Short Tale

from colorama import Fore
import sys, time, random
from datetime import datetime

l01 = "                	     	      	    .-."
l02 = "		                               {{@}}"
l03 = "		               <>               8@8"
l04 = "		             .::::.             888"
l05 = "		         @\\\/W\/\/W\//@         8@8"
l06 = "		          \\\/^\/\/^\//     _    )8(    _"
l07 = "		           \_O_<>_O_/     (@)__/8@8\__(@)"
l08 = "		      ____________________ `~\"-=):(=-\"~`"
l09 = "		     |<><><>  |  |  <><><>|     |.|"
l10 = "		     |<>      |  |      <>|     |Y|"
l11 = "		     |<>      |  |      <>|     |'|"
l12 = "		     |<>   .--------.   <>|     |.|"
l13 = "		     |     |   ()   |     |     |E|"
l14 = "		     |_____| (O\/O) |_____|     |'|"
l15 = "		     |     \   /\   /     |     |.|"
l16 = "		     |------\  \/  /------|     |E|"
l17 = "		     |   BY  '.__.'       |     |'|"
l18 = "		     |        |  |        |     |.|"
l19 = "		     :  JOHN  |  |STAFFORD:     |T|"
l20 = "		      \<>     |  |     <>/      |'|"
l21 = "		       \<>    |  |    <>/       |.|"
l22 = "		        \<>   |  |   <>/        |!|"
l23 = "		         `\<> |  | <>/'         |'|"
l24 = "		           `-.|  |.-`           \ /"
l25 = "	                      '--'               ^"

class Game():
	def __init__(self):
		#Initialize game class, to hold variables for the user. This includes progress for saving, and other clever things John will think of. 
		self.chapter = 1
		self.prog = 0
		self.choices = {"Chapter1":{},
		   "Chapter2":{},
		   "Chapter3":{},
		   "Chapter4":{},
		   "Chapter5":{},
		   "Chapter6":{}}
		
	def make_choice(self, name, question ,*args, secret = []):
		secret = [i.upper() for i in secret]
		print(Fore.CYAN + question)	
		for j, i in enumerate(args):
			print(Fore.GREEN + "{}: {}".format(chr(65 + j), i))
		ans = input("").upper()
		if "save" in ans.lower():
			split_save = ans.lower().split(" ")
			name = " ".join(split_save[1:])
			if name == "":
				save_progress()
			else:
				save_progress(name)		
		if ans in secret:
			self.choices["Chapter1"].update({name:ans})
			return ans
		if ans == "QUIT":
			quit()
		while ans not in [chr(65 + i) for i in range(len(args))]:	
			if "save" not in ans.lower():
				print(Fore.RED + "Please enter a valid response!\n")
			print(Fore.CYAN + question)
			for j, i in enumerate(args):
				print(Fore.GREEN + "{}: {}".format(chr(65 + j), i))	
			ans = input("").upper()	
			if "save" in ans.lower():
				split_save = ans.lower().split(" ")
				name = " ".join(split_save[1:])
				if name == "":
					save_progress()
				else:
					save_progress(name)		
			if ans in secret:
				self.choices["Chapter1"].update({name:ans})
				return ans
			if ans == "QUIT":
				quit()
		self.choices["Chapter1"].update({name:args[ord(ans) - 65]})
		return ans
			

game = Game()

def save_progress(name = "AutoSave", quiet = False):
	
	if name == "AutoSave":
		name = name + datetime.now().strftime(" at %H.%M on %d-%m")
	
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
	save_file.write(str(game.chapter + game.prog))
	save_file.write("\n")
					
	save_file.write("#CHOICES\n")
	save_file.write(str(game.choices))
		
	save_file.close()
	
	if not quiet:
		print("Saved progress!")
	time.sleep(1)

from auxscripts.init import Hero

player = Hero("NONAME", "NOCLASS")

#Auxillary scripts6
from auxscripts.fullscreen import AltENTER #To go full screen
from auxscripts.MUSTFUNC import art, kart, main #VERY IMPORT FUNCTIONS TO THE STORY

import os

#Chapters
from chapters.Chapter1 import chapter1

clear = lambda: os.system('cls')

def quit():
	print("Thank you for playing!")
	time.sleep(2)
	sys.exit()	
#%%
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

AltENTER() #Make full screen.
		  
kart() #Animation
clear() #Clear cmd 
art() #Create menu art

player, story = main(player) #In MUSTFUNC, says new/load

game.chapter = int(story)
game.prog = story - game.chapter
game.prog = round(game.prog , 2)

print("\n")
print(Fore.CYAN + "---------")
time.sleep(0.3)
print(Fore.CYAN + "Chapter 1")
time.sleep(0.3)
print(Fore.CYAN + "---------\n" + Fore.GREEN)

time.sleep(2)

chapter1(player)
