"""
Menu Functions

	+) Things that I reuse in almost everything.
"""
import os

def clear():
	"""Clears screen"""
	osName = os.name
	if osName == 'posix':
		os.system('clear')
	elif osName == 'dos' or osName == 'nt':
		os.system('cls')
