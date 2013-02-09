#!/usr/bin/python
"""
Program: File Convert

Can run ffmpeg and lame on a directory of flv files.
"""
import os
import sys
import subprocess

def mainMenu():
	print '1) ffmpeg'
	print '2) lame'
	print '3) move mp3s'
	print '4) exit'
	menuAnswer = input('--> ')
	return menuAnswer

def main(menuAnswer):
	if menuAnswer == 1:
		directory = raw_input('Directory: ')
		for each in os.listdir(directory):
			if '.flv' in each:
				newName = '.'.join([each[:-4],'wav'])
				print each, newName
				subprocess.call(['ffmpeg', '-i', each, newName])
			elif '.mp4' in each:
				newName = '.'.join([each[:-4],'wav'])
				print each, newName
				subprocess.call(['ffmpeg', '-i', each, newName])

	elif menuAnswer == 2:
		directory = raw_input('Directory: ')
		for each in os.listdir(directory):
			if '.wav' in each:
					newName = '.'.join([each[:-4],'mp3'])
					print each, newName
					subprocess.call(['lame', each, newName])

	elif menuAnswer == 3:
		subprocess.Popen(['mkdir','mp3s','flvWavMp4'])
		subprocess.Popen(['mv *.flv *.wav *.mp4 flvWav'], shell=True)
		subprocess.Popen(['mv *.mp3 mp3s'], shell=True)

	elif menuAnswer == 4:
		exit()				

while True:
	main(mainMenu())