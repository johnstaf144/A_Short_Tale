from colorama import Fore
from auxscripts.read import load #load
from auxscripts.func import jinput #Useful functions
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
	
def kprint(s, t = 0.05):
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
	kprint("  	     		                           .-.                                                   ")
	kprint(" 	      		                          {{@}}")
	kprint(" 	     		          <>               8@8")
	kprint(" 	     		        .::::.             888")
	kprint(" 	     		    @\\\/W\/\/W\//@         8@8")
	kprint(" 	     		     \\\/^\/\/^\//     _    )8(    _")
	kprint(" 	     		      \_O_<>_O_/     (@)__/8@8\__(@)")
	kprint(" 	     		 ___________________ `~\"-=):(=-\"~`")
	kprint(" 	     		|<><><>  |  |  <><><>|     |.|")
	kprint(" 	     		|<>      |  |      <>|     |Y|")
	kprint(" 	     		|<>      |  |      <>|     |'|")
	kprint(" 	     		|<>   .--------.   <>|     |.|")
	kprint(" 	     		|     |   ()   |     |     |E|")
	kprint(" 	     		|_____| (O\/O) |_____|     |'|")
	kprint(" 	     		|     \   /\   /     |     |.|")
	kprint(" 	     		|------\  \/  /------|     |E|")
	kprint(" 	     		|   BY  '.__.'       |     |'|")
	kprint(" 	     		|        |  |        |     |.|")
	kprint(" 	                     :  JOHN  |  |STAFFORD:     |T|")
	kprint("          		         \<>     |  |     <>/      |'|")
	kprint("  	      		  \<>    |  |    <>/       |.|")
	kprint("   	     		   \<>   |  |   <>/        |!|")
	kprint("  	     	 	    `\<> |  | <>/'         |'|")
	kprint("   	     		      `-.|  |.-`           \ /")
	kprint("         		         '--'               ^ ")


def main():
	jinput("Press enter key to start: ")
	new_game = jinput("New game/load chapter? [new/load]:")
	if new_game == "new":
		story_progress = 1.0
	elif new_game == "load":
		player, story_progress, Choices = load()
	else:
		print(required)
		print("")
		print("Restarting")
		time.sleep(1)
		main()
	return story_progress
		
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