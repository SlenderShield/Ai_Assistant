import requests
import wikipedia
import pywhatkit
from email.message import EmailMessage
import smtplib
import wolframalpha
from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")


def find_my_ip():
	""" Function to get the current IP address"""
	ip_address = requests.get("https://api64.ipify.org/?format=json")
	return ip_address["ip"]


def search_wikipedia(query):
	""" Function to search query in wikipedia"""
	search = wikipedia.summary(query, sentence=5)
	return search


def youtube_play(video):
	""" Function to Play video on YouTube"""
	pywhatkit.playonyt(video)


def search_google(query):
	"""Function to search query on Google """
	pywhatkit.search(query)


def send_whatsapp_message(number, message):
	"""Function to send whatsapp messages instantly"""
	pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)


def send_email(receiver_address, subject, message):
	"""Function to send email to specified receiver"""
	try:
		email = EmailMessage()
		email['To'] = receiver_address
		email['Subject'] = subject
		email['From'] = EMAIL
		email.set_content(message)

		smtp = smtplib.SMTP("smtp.gmail.com", 587)
		smtp.starttls()
		smtp.login(EMAIL, PASSWORD)
		smtp.send_message(email)
		smtp.close()
		return True
	except Exception as e:
		print(e)
		return False


def get_latest_news():
	""" Function to get the top news of the date"""
	news_headlines = []
	# Receive the news in json formate
	result = requests.get(
		f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
	articles = result["articles"]
	for article in articles:
		news_headlines.append(article["title"])
	return news_headlines[:]  # return all the headlines


def get_weather_report(city):
	"""Function to get the weather report of the city"""
	result = requests.get(
		f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
	weather = result["weather"][0]["main"]
	temperature = result["main"]["temp"]
	feels_like = result["main"]["feels_like"]
	return weather, f"{temperature}℃", f"{feels_like}℃"


def get_trending_movies():
	"""Function to get the top trending movies"""
	trending_movies = []
	result = requests.get(
		f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
	results = result["results"]
	for result in results:
		trending_movies.append(result["Original_title"])
	return trending_movies[:]


def get_random_joke():
	"""Function that returns a random joke"""
	headers = {
		'Accept': 'application/json'
	}
	result = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
	return result["joke"]


def get_random_advice():
	result = requests.get("https://api.adviceslip.com/advice").json()
	return result["slip"]["advice"]


def get_wolframalpha(query):
	""" Function to get the computational answers"""
	WOLFRAMALPHA_API = config('WOLFRAMALPHA_API')
	client = wolframalpha.Client(WOLFRAMALPHA_API)
	res = client.query(query)
	answer = next(res.results).text
	return answer
