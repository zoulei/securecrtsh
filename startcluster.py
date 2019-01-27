#$language = "Python"
#$interface = "1.0"

import os

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("cd pccppdocker/build && bash rundocker.sh\n")
	crt.Screen.Send("./Main\n")
	crt.Screen.Send("exit\n")
	# crt.Screen.Send("htop\n")
Main()