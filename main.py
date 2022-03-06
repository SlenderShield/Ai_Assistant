import pyttsx3
from decouple import config
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, \
	get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, \
	get_wolframalpha
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord, open_webstorm, \
	open_pycharm, shutdown
from pprint import pprint
import speech_recognition as sr
from random import choice
from utils import opening_text

USER = config('USER')
BOT = config('BOT')

# Initialize the engine
# The "sapi5" is the Microsoft Speech API
engine = pyttsx3.init('sapi5')

# Set rate and volume
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# Set voice to Female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
	"""Used to speak the text to the user which is passed to it"""
	engine.say(text)
	engine.runAndWait()  # waits till all the commands as done.


def take_user_input():
	""" Takes user input using the Speech Recognition"""
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening.....")
		r.pause_threshold = 2  # Time till request from assistant
		audio = r.listen(source)

	# Try to recognize the request
	try:
		print("Recognizing....")
		query = r.recognize_google(audio, language='us-in')
		if not "exit" in query or not "stop" in query:
			speak(choice(opening_text))
		else:
			hour = datetime.now().hour
			if hour >= 21 and hour < 6:
				speak("Good night sir, take care!")
			else:
				speak('Have a good day sir!')
			exit()
	# if request is not recognized
	except Exception:
		speak("Sorry, I could not understand. Could you please repeat")
		query = "None"
	return query


def greet_user():
	"""Greets the user according to the current time"""
	hour = datetime.now().hour  # take hour value of the time

	# Greet according to the time
	if (hour >= 6) and (hour < 12):
		speak(f"Good Morning {USER}")
	elif (hour >= 12) and (hour < 16):
		speak(f"Good Afternoon {USER}")
	elif (hour >= 16) and (hour < 21):
		speak(f"Good Evening {USER}")

	speak(f"I am {BOT}. How many i assist you")


if __name__ == '__main__':
	greet_user()
	while True:
		query = take_user_input().lower()

		if 'open pycharm' in query:
			open_pycharm()

		elif 'open webstorm' in query:
			open_webstorm

		elif 'open discord' in query:
			open_discord()

		elif 'shutdown' in query:
			shutdown()

		elif 'open command prompt' in query or 'open cmd' in query:
			open_cmd()

		elif 'open camera' in query:
			open_camera()

		elif 'open calculator' in query:
			open_calculator()

		elif 'ip address' in query:
			ip_address = find_my_ip()
			speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
			print(f'Your IP Address is {ip_address}')

		elif 'wikipedia' in query:
			speak('What do you want to search on Wikipedia, sir?')
			search_query = take_user_input().lower()
			results = search_on_wikipedia(search_query)
			speak(f"According to Wikipedia, {results}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(results)

		elif 'youtube' in query:
			speak('What do you want to play on Youtube, sir?')
			video = take_user_input().lower()
			play_on_youtube(video)

		elif 'search on google' in query:
			speak('What do you want to search on Google, sir?')
			query = take_user_input().lower()
			search_on_google(query)

		elif "send whatsapp message" in query:
			speak('On what number should I send the message sir? Please enter in the console: ')
			number = input("Enter the number: ")
			speak("What is the message sir?")
			message = take_user_input().lower()
			send_whatsapp_message(number, message)
			speak("I've sent the message sir.")

		elif "send an email" in query:
			speak("On what email address do I send sir? Please enter in the console: ")
			receiver_address = input("Enter email address: ")
			speak("What should be the subject sir?")
			subject = take_user_input().capitalize()
			speak("What is the message sir?")
			message = take_user_input().capitalize()
			if send_email(receiver_address, subject, message):
				speak("I've sent the email sir.")
			else:
				speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

		elif 'joke' in query:
			speak(f"Hope you like this one sir")
			joke = get_random_joke()
			speak(joke)
			speak("For your convenience, I am printing it on the screen sir.")
			pprint(joke)

		elif "advice" in query:
			speak(f"Here's an advice for you, sir")
			advice = get_random_advice()
			speak(advice)
			speak("For your convenience, I am printing it on the screen sir.")
			pprint(advice)

		elif "trending movies" in query:
			speak(f"Some of the trending movies are: {get_trending_movies()}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(*get_trending_movies(), sep='\n')

		elif 'news' in query:
			speak(f"I'm reading out the latest news headlines, sir")
			speak(get_latest_news())
			speak("For your convenience, I am printing it on the screen sir.")
			print(*get_latest_news(), sep='\n')

		elif 'weather' in query:
			ip_address = find_my_ip()
			city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
			speak(f"Getting weather report for your city {city}")
			weather, temperature, feels_like = get_weather_report(city)
			speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
			speak(f"Also, the weather report talks about {weather}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

		elif 'compute' in query:
			speak('I can answer to computational and geographical questions to. Just try me')
			speak('What do you want to compute')
			answer = get_wolframalpha(query)
			speak(answer)
			print(answer)
