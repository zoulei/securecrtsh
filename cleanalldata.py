#$language = "Python"
#$interface = "1.0"

import os

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("bash ../sh/cleancollaboration.sh\n")
	crt.Screen.Send("bash ../sh/cleancollaborationdata.sh\n")
	# crt.Screen.Send("htop\n")
Main()