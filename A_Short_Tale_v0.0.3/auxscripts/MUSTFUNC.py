from colorama import Fore
from auxscripts.read import load #load
from auxscripts.func import jinput #Useful functions
from __main__ import game, player
from auxscripts.values import required, no
import time, os

clear = lambda: os.system('cls')

def art():
	print(Fore.GREEN)
	clear()
	print(Fore.YELLOW + "               (         )      )    (                                      (           ")
	print(Fore.RED + "   (           )\ )   ( /(   ( /(    )\ )    *   )        *   )     (       )\ )        ")
	print("   )\         (()/(   )\())  )\())  (()/(  ` )  /(      ` )  /(     )\     (()/(   (    ")
	print("((((_)(        /(_)) ((_)\  ((_)\    /(_))  ( )(_))      ( )(_)) ((((_)(    /(_))  )\   ")
	print(" )\ _ )\      (_))    _((_)   ((_)  (_))   (_(_())      (_(_())   )\ _ )\  (_))   ((_)  "+ Fore.GREEN)
	print(" (_)_\(_)     / __|  | || |  / _ \  | _ \  |_   _|      |_   _|   (_)_\(_) | |    | __| ")
	print("  / _ \       \__ \  | __ | | (_) | |   /    | |          | |      / _ \   | |__  | _|  ")
	print(" /_/ \_\      |___/  |_||_|  \___/  |_|_\    |_|          |_|     /_/ \_\  |____| |___| ")
	print("""                	     	  	         	.-.
			                               {{@}}
			               <>               8@8
			             .::::.             888
			         @\\\/W\/\/W\//@         8@8
			          \\\/^\/\/^\//     _    )8(    _
			           \_O_<>_O_/     (@)__/8@8\__(@)
			      ____________________ `~"-=):(=-"~`
			     |<><><>  |  |  <><><>|     |.|
			     |<>      |  |      <>|     |Y|
			     |<>      |  |      <>|     |'|
			     |<>   .--------.   <>|     |.|
			     |     |   ()   |     |     |E|
			     |_____| (O\/O) |_____|     |'|
			     |     \   /\   /     |     |.|
			     |------\  \/  /------|     |E|
			     |   BY  '.__.'       |     |'|
			     |        |  |        |     |.|
			     :  JOHN  |  |STAFFORD:     |T|
			      \<>     |  |     <>/      |'|
			       \<>    |  |    <>/       |.|
			        \<>   |  |   <>/        |!|
			         `\<> |  | <>/'         |'|
			           `-.|  |.-`           \ /
			              '--'               ^ """)
	
def kprint(s, t = 0.02):
	print(s)
	time.sleep(t)


def kart():
	kprint(Fore.GREEN)
	clear()
	kprint(Fore.YELLOW + "               (         )      )    (                                      (           ")
	kprint(Fore.RED + "   (           )\ )   ( /(   ( /(    )\ )    *   )        *   )     (       )\ )        ")
	kprint("   )\         (()/(   )\())  )\())  (()/(  ` )  /(      ` )  /(     )\     (()/(   (    ")
	kprint("((((_)(        /(_)) ((_)\  ((_)\    /(_))  ( )(_))      ( )(_)) ((((_)(    /(_))  )\   ")
	kprint(" )\ _ )\      (_))    _((_)   ((_)  (_))   (_(_())      (_(_())   )\ _ )\  (_))   ((_)  "+ Fore.GREEN)
	kprint(" (_)_\(_)     / __|  | || |  / _ \  | _ \  |_   _|      |_   _|   (_)_\(_) | |    | __| ")
	kprint("  / _ \       \__ \  | __ | | (_) | |   /    | |          | |      / _ \   | |__  | _|  ")
	kprint(" /_/ \_\      |___/  |_||_|  \___/  |_|_\    |_|          |_|     /_/ \_\  |____| |___| ")
	kprint("                	     	  	         	.-.                                                   ")
	kprint("			                               {{@}}")
	kprint("			               <>               8@8")
	kprint("			             .::::.             888")
	kprint("			         @\\\/W\/\/W\//@         8@8")
	kprint("			          \\\/^\/\/^\//     _    )8(    _")
	kprint("			           \_O_<>_O_/     (@)__/8@8\__(@)")
	kprint("			      ____________________ `~\"-=):(=-\"~`")
	kprint("			     |<><><>  |  |  <><><>|     |.|")
	kprint("			     |<>      |  |      <>|     |Y|")
	kprint("			     |<>      |  |      <>|     |'|")
	kprint("			     |<>   .--------.   <>|     |.|")
	kprint("			     |     |   ()   |     |     |E|")
	kprint("			     |_____| (O\/O) |_____|     |'|")
	kprint("			     |     \   /\   /     |     |.|")
	kprint("			     |------\  \/  /------|     |E|")
	kprint("			     |   BY  '.__.'       |     |'|")
	kprint("			     |        |  |        |     |.|")
	kprint("			     :  JOHN  |  |STAFFORD:     |T|")
	kprint("			      \<>     |  |     <>/      |'|")
	kprint("			       \<>    |  |    <>/       |.|")
	kprint("			        \<>   |  |   <>/        |!|")
	kprint("			         `\<> |  | <>/'         |'|")
	kprint("			           `-.|  |.-`           \ /")
	kprint("			              '--'               ^ ")
	
def pprint(s):
	time.sleep(0.5)
	for i in range(len(s)):
		print(s[:i+1], end="\r")
		time.sleep(random.randint(1, 10)/100)
	print("\n")

def main(player):
	jinput("Press enter key to start: ")
	new_game = jinput("New game/load chapter? [new/load]:")
	if new_game == "new":
		story_progress = 1.0
	elif new_game == "load":
		path_to_dir = os.path.abspath(".")
		saves = os.walk(path_to_dir + "/saveData")
		pprint("Here are your saved files.")
		for x in saves:
			for j, file in enumerate(x[2]):
				pprint("{}: {}".format(j + 1, file[:-4]))
		file_number = input("Which file do you choose? ")
		while file_number not in [str(i) for i in range(1, len(x[2]) + 1)]:
			file_number = input("Please pick again!\nWhich file do you choose? ")
		file = x[2][int(file_number) - 1]
		player, story_progress, choices = load(file)
		game.choices = choices
		pprint("Welcome back, {}!".format(player.name))
		time.sleep(1)
	else:
		pprint(required)
		print("")
		pprint("Restarting")
		time.sleep(1)
		main(player)
	return player, story_progress
		
def death():
	death = jinput ("You died, would you like to start again... or get up!?: ")
	if death == "yes":
		pass
	elif death in no:
		quit()
	elif death == "NOOO" or death == "get up" or death == "NO" or death == "stand up":
		pass
		#strength
		#constitution += 2 
		#hardy()