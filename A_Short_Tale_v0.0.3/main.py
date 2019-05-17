#Main file for A Short Tale
import os
import ctypes.wintypes as wintypes
from colorama import Fore
import ctypes
import msvcrt
import subprocess
import time

#Auxillary scripts
from auxscripts.fullscreen import * #To go full screen
from auxscripts.init import * #Initialise game
from auxscripts.MUSTFUNC import * #VERY IMPORT FUNCTIONS TO THE STORY
from auxscripts.func import * #Useful functions
from auxscripts.values import * #Values

#Chapters
from chapters.Chapter1 import *

AltENTER() #Make full screen.
		  
kart()
clear()
art()
      
main()

dream()