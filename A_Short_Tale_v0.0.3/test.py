import time
import random

def pprint(s):
	time.sleep(1)
	for i in range(len(s)):
		print(s[:i+1], end="\r")
		time.sleep(random.randint(2, 10)/100)
		
pprint("Emma Langfield, are you there??")
time.sleep(3)
pprint("Please respond...")

time.sleep(5)
