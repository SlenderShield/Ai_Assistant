# The required libraries
# import os
import time
import subprocess
# import json

import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime

import speech_recognition as sr
import pyttsx3

load = 'Loading your personal assistant'
print(load)

engine = pyttsx3.init('sapi5')  # 'nsss' for the ios devices
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0]')  # 0 for a voice of man, 1 for voice of a women


def speak(text):
	"""function to let the ai speak"""
	engine.say(text)  # the speech engine say what is given in as text
	engine.runAndWait()


def wish_me():
	hour = datetime.datetime.now().hour
	if 0 <= hour <= 12:
		speak('Hello, Good Morning')
		print('Hello, Good Morning')
	elif 12 < hour < 16:
		speak('Hello, Good Afternoon')
		print('Hello, Good Afternoon')
	elif hour >= 22:
		speak("Sir, It's already past 10 PM. Time to go to bed")
		print("Sir, It's 10 PM. Time to go to bed")
	else:
		speak('Hello, Good Evening')
		print('Hello, Good Evening')


def take_command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('I am Listening')
		audio = r.listen(source)
		# noinspection PyBroadException
		try:
			command = r.recongize_google(audio, language='en-in')
			print(f'user said:{command}\n')
		except Exception:
			speak('Pardon me, please repeat')
			return 'None'
		return command


speak(load)
wish_me()

if __name__ == '__main__':
	while True:
		speak('How may i help you')
		statement = take_command().lower()
		if statement == 0:
			continue
		if 'Good bye' in statement or 'Bye' in statement or 'stop' in statement:
			speak('Your ai assistant is logging off')
			print('Your ai assistant is logging off')
			break

		if 'wikipedia' in statement:
			speak('searching wikipedia.....')
			statement = statement.replace('wikipedia', '')
			results = wikipedia.summary(statement, sentences=5)
			speak('According to the wikipedia...')
			speak(results)
			print(results)
		elif 'Open youtube' in statement:
			webbrowser.open_new_tab('https://youtube.com')
			speak('Youtube is open for you')
			print('Youtube is open for you')
			time.sleep(5)

		elif 'Open google' in statement:
			webbrowser.open_new_tab('https://google.com')
			speak('Google search is open for you')
			print('Google search is open for you')
			time.sleep(5)

		elif 'open gmail' in statement:
			webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
			speak('Your mail is open for you')
			time.sleep(5)

		elif 'weather' in statement:
			api_key = 'f60ebcd1444ec94ac1fd185f2d9095ab'  # api key
			base_url = 'https://api.openweathermap.org/data/2.5/weather?'
			speak('Whats the city name')
			city = take_command()
			url = base_url + "&q=" + city + 'apiid' + api_key
			response = requests.get(url)
			report = response.json()
			if report['cod'] != '404':
				weather = report['main']
				temperature = weather['temp']
				humidity = weather['humidity']
				getDescription = weather['weather']
				description = getDescription[0]['description']
				speak('The temperature in kelvin is' + str(temperature))
				speak('The Humidity in percentage is' + str(humidity))
				speak('Weather description' + str(description))
				print('The temperature in kelvin is' + str(temperature))
				print('The Humidity in percentage is' + str(humidity))
				print('Weather description' + str(description))
			else:
				speak('Sorry sir, The city not found')
				print('Sorry sir, The city not found')

		elif 'time' in statement:
			time_now = datetime.datetime.now().strftime("%H:%M:%S")
			speak(time_now)
			print(f'The time is{time_now}')

		elif 'who are you' in statement or 'what can you do' in statement:
			speak("I am your ai assistant. I am programed to work for you and help you in your task")

		elif 'who built you' in statement or 'who made you' in statement or 'who created you' in statement:
			speak('Mr Muralidhara Bhat is my creator.')
			print('Mr Muralidhara Bhat is my creator.')

		elif 'open stack overflow' in statement:
			webbrowser.open_new_tab('https://stackoverflow.com/login')
			time.sleep(5)

		elif 'news' in statement:
			news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
			speak('Here are some headline for you' + str(news))
			time.sleep(4)

		elif 'search' in statement:
			search = statement.replace('search', '')
			webbrowser.open_new_tab('statement')
			time.sleep(5)

		elif 'ask' in statement:
			speak('I can answer to computational and geographical questions to. Just try me')
			speak('What do you want to compute')
			question = take_command()
			wolframaplha_api = 'P7U55Q-3R2V63JRQV'
			client = wolframalpha.Client(wolframaplha_api)
			res = client.query(question)
			answer = next(res.results).text
			speak(answer)
			print(answer)

		elif 'Shutdown' in statement or 'log off' in statement or 'sign out' in statement:
			speak('Okay, Your PC will shut down in 10 seconds')
			speak('Make sure your works are saved')
			subprocess.call(['Shutdown', '/1'])

time.sleep(3)
