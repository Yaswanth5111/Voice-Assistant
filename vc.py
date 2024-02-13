import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
import json
# Initialize the speech recognition module
recognizer = sr.Recognizer()
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Create the main window
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("500x400")
window.configure(bg="#1f1f1f")
# Create a label to display the assistant's responses
response_label = tk.Label(window, text="Assistant: ", font=("Arial", 14), wraplength=400)
response_label.pack(pady=20)
voices = engine.getProperty('voices')
# Set the name of the voice assistant
assistant_name = "Optimus Prime"
# Find the voice that closely resembles Optimus Prime's voice
for voice in voices:
    if "male" in voice.name.lower() and "english" in voice.name.lower() and "united states" in
    voice.name.lower():
    engine.setProperty('voice', voice.id)
    break
# Function to speak text
def speak(text):
    engine.say(text)
engine.runAndWait()
# Set the voice assistant's name
print(f"I am {assistant_name}, your virtual assistant. How can I assist you today?")
speak(f"I am {assistant_name}, your virtual assistant. How can I assist you today?")
# Define function for listening and understanding user input
# Function to listen for user commands
def listen_for_command():
with sr.Microphone() as source:
print("Listening...")
recognizer.adjust_for_ambient_noise(source)
audio = recognizer.listen(source)
try:
# Convert speech to text
command = recognizer.recognize_google(audio)
print("User Command:", command)
# Process the user's command and generate a response
response = process_command(command)
# Update the response label
response_label.config(text="Assistant: " + response)
# Convert the response to speech
speak(response)
except sr.UnknownValueError:
print("Sorry, I could not understand your command.")
except sr.RequestError as e:
print("Sorry, an error occurred while processing your command.")
# Function to generate a response based on the user's command
def process_command(command):
response = ""
if 'hello' in command:
response = "Hello! How can I assist you today?"
elif 'time' in command:
current_time = datetime.datetime.now().strftime("%I:%M %p")
response = "The current time is " + current_time
elif 'weather' in command:
response = get_weather()
elif 'search' in command:
search_query = command.replace('search', '')
response = "Searching for '" + search_query + "' on the internet..."
webbrowser.open("https://www.google.com/search?q=" + search_query)
elif 'play' in command:
song = command.replace('play', '')
response = "Playing " + song + " on YouTube..."
webbrowser.open("https://www.youtube.com/results?search_query=" + song)
elif 'volume' in command:
if 'up' in command:
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 0.1)
response = "Volume increased"
elif 'down' in command:
volume = engine.getProperty('volume')
engine.setProperty('volume', volume - 0.1)
response = "Volume decreased"
elif 'max' in command:
engine.setProperty('volume', 1.0)
response = "Volume set to maximum"
elif 'location' in command or 'current location' in command:
response = get_current_location()
elif 'history' in command or 'commands history' in command:
response = show_commands_history()
elif 'news' in command or 'daily news' in command:
response = get_daily_news()
elif 'calculate' in command or 'calculation' in command:
calculate_expression(command)
else:
response = "Sorry, I could not understand your command."
return response
# Function to convert text to speech
def speak(text):
engine.say(text)
engine.runAndWait()
# Function to get the current weather
def get_weather():
try:
    api_key = 'your_api_key_here'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "New York"
complete_url = base_url + "q=" + city_name + "&appid=" + api_key
response = requests.get(complete_url)
data = response.json()
if data["cod"] != "404":
main_data = data["main"]
temperature = round(main_data["temp"] - 273.15, 2)
weather_data = data["weather"][0]
weather_description = weather_data["description"]
return f"The weather in {city_name} is {weather_description} with a temperature of
{temperature}°C."
else:
return "Sorry, I could not fetch the weather information."
except Exception as e:
return "Sorry, an error occurred while fetching the weather information."
# Function to get the current location
def get_current_location():
try:
url = "https://ipinfo.io/json"
response = requests.get(url)
data = json.loads(response.text)
location = f"You are currently in {data['city']}, {data['region']}, {data['country']}"
return location
except Exception as e:
return "Sorry, I could not fetch the location."
# Function to show the history of commands
def show_commands_history():
# Implement logic to retrieve and display the history of commands
# For demonstration purposes, we'll print a dummy history
command_history = [
"search for the weather",
"play some music",
"open YouTube",
"calculate 5 plus 3",
"current location"
]
response = "Here are your previous commands:\n"
for idx, command in enumerate(command_history, start=1):
response += f"{idx}. {command}\n"
return response
def calculate_expression(command):
expression = command.replace('calculate', '').strip()
try:
result = eval(expression)
speak(f"The result is {result}")
print(f"The result is {result}")
except Exception as e:
speak("Sorry, I could not calculate that.")
# Function to get daily news
def get_daily_news():
try:
url =
'https://newsapi.org/v2/top-headlines?country=us&apiKey=967057fb48d3408bbd8a29ce2ab2b11c'
response = requests.get(url)
data = response.json()
articles = data["articles"] [:5]
response = "Here are the top news headlines:\n"
for idx, article in enumerate(articles, start=1):
print(f"News {idx}: {article['title']}")
speak(f"News {idx}: {article['title']}")
return response
except Exception as e:
return "Sorry, I could not fetch the news."
response_label = tk.Label(window, text="Genie: ", font=("Arial", 14), wraplength=400,
fg="#00ff00", bg="#1f1f1f")
response_label.pack(pady=20)
# Create a button to start listening
listen_button = tk.Button(window, text="Listen", font=("Arial", 14),
command=listen_for_command)
listen_button.pack(pady=20)
# Create a button to stop the assistant
stop_button = tk.Button(window, text="Stop", font=("Arial", 14), bg="#FF0000", fg="#000000",
command=window.destroy)
stop_button.pack(pady=10)