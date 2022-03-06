import os
import subprocess as sp

paths = {
	'pycharm': "C:\Program Files\JetBrains\PyCharm 2021.2.2\bin\pycharm64.exe",
	'webstorm': "C:\Program Files\JetBrains\WebStorm 2021.2.2\bin\webstorm64.exe",
	'discord': "C:\Users\ksmur\AppData\Local\Discord\Update.exe",
	'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
	# Function to open camera
	sp.run('start microsoft.windows.camera:', shell=True)


def open_pycharm():
	# Function to open pycharm
	os.starfile(paths['pycharm'])


def open_webstorm():
	# Function to open WebStorm
	os.starfile(paths['webstorm'])


def open_discord():
	# Function to open discord
	os.stat_result(paths['discord'])


def open_cmd():
	# Function to open command prompt
	os.system('start cmd')


def open_calculator():
	# Function to open calculator
	sp.Popen(paths['calculator'])


def shutdown():
	# Function to shut down the computer
	sp.call(['Shutdown', '/1'])
