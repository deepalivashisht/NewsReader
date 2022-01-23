import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

speak("Welcome to the BBC News Channel")
speak("Please enter your news api key first..")
Api_key=input("Enter News API Key: ")
url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey="
#dbf07b522fd643b487e470e3b967c2f7
url = url+Api_key
data = requests.get(url)
news_dict = data.json()
news = news_dict['articles']
speak("Here are the top ten news of the world...")
speak("So our first news is ")
for i in range(1,11):
    print(i)
    print(news[i]['description'])
    speak(news[i]['description'])
    if i>=11:
        break
    time.sleep(1)
    if i==10:
        speak("So our last news is ")
    else:
        speak("Moving on to the next news...")

speak("Thanks for listening ! Have a nice day")
speak("stay happy and keep coding")