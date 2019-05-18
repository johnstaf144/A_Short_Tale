from colorama import Fore

#Auxillary scripts
from auxscripts.fullscreen import * #To go full screen
from auxscripts.init import * #Initialise game
from auxscripts.MUSTFUNC import * #VERY IMPORT FUNCTIONS TO THE STORY
from auxscripts.func import * #Useful functions
from auxscripts.values import * #Values

required = (Fore.RED + """
Please enter a valid response""" + Fore.GREEN) #random response

answer_A = ["A" , "a"]
answer_B = ["B" , "b"]
answer_C = ["C" , "c"]
answer_D = ["D", "d"]
yes = ["yes" , "Yes", "YES"]
no = ["No" , "no"]
comp_n = ["North", "n", "N", "north"]
comp_w = ["West", "west", "w", "W"]
comp_e = ["east" , "East" , "e" , "E"]
comp_s = ["South" , "south", "s", "S"]

l_quit = ["quit", "exit"]

choices = {"Chapter1":{},
		   "Chapter2":{},
		   "Chapter3":{},
		   "Chapter4":{},
		   "Chapter5":{},
		   "Chapter6":{}}