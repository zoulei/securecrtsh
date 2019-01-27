#$language = "Python"
#$interface = "1.0"

import os

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("cd pccppdocker/build && bash snap.sh\n")
	crt.Screen.Send("make && ./Main\n")
	# crt.Screen.Send("htop\n")
Main()