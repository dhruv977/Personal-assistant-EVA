import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import smtplib
import shutil
import ctypes
import winshell
from email.message import EmailMessage
from selenium import webdriver
import os
import wolframalpha
import subprocess
import requests


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        voice = listener.listen(source)

        try:
            print("Recognizing...")
            query = listener.recognize_google(audio_data=voice, language='en-in')
            query = query.lower()
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

    return query


def username():
    talk("What should i call you?")
    uname = take_command()
    talk("Welcome" + uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    talk("How can i help you?")


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning !")

    elif 12 <= hour < 18:
        talk("Good Afternoon !")

    else:
        talk("Good Evening !")

    ass_name = "Eva"
    talk("I am your Assistant")
    talk(ass_name)


def sendmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Enable low security in gmail
    server.login('arora6190@gmail.com', 'dhruv@1005')
    email = EmailMessage()
    email['From'] = 'arora6190@gmail.com'
    email['To'] = to
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)


email_list = {
    'garima': 'somani.garima123@gmail.com'
}


def run_eva():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Its' + time)

    elif 'who is' in command:
        query = command.replace('who is', '')
        info = wikipedia.summary(query, 1)
        print(info)
        talk(info)

    elif 'wikipedia' in command:
        if 'open' in command:
            launch = command.replace('open', '')
            talk('opening' + launch)
            webbrowser.open('wikipedia.com')
        else:
            talk('Searching Wikipedia...')
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            talk("According to Wikipedia")
            print(results)
            talk(results)

    elif 'open google' in command:
        launch = command.replace('open', '')
        talk('opening' + launch)
        webbrowser.open('google.com')

    elif 'open youtube' in command:
        launch = command.replace('open', '')
        talk('opening' + launch)
        webbrowser.open('youtube.com')

    elif 'open stack overflow' in command:
        launch = command.replace('open', '')
        talk('opening' + launch)
        webbrowser.open('stackoverflow.com')

    elif 'youtube' in command:
        browser = webdriver.Chrome()
        talk("Opening in youtube")
        indx = command.lower().split().index('youtube')
        query = command.split()[indx + 1:]
        browser.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        while True:
            pass

    elif 'search' in command:
        query = command.replace("search", "")
        webbrowser.open(query)

    elif 'send a mail' in command:
        def mail_info():
            try:
                talk("Whom should i send")
                name = take_command()
                to = email_list[name]
                print(to)
                talk('Tell me the subject of your email?')
                subject = take_command()
                talk("What should I say?")
                content = take_command()
                sendmail(to, subject, content)
                talk("Email has been sent !")
            except Exception as e:
                print(e)
                talk("I am not able to send this email")

        mail_info()
        talk("Do you want send more?")
        send_more = take_command()
        if 'yes' in send_more:
            mail_info()

    elif "news" in command:

        complete_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=7821bb8e903843dea7d4e56a28017016"
        news = requests.get(complete_url).json()
        articles = news["articles"]
        news_art = []
        for article in articles:
            news_art.append(article["title"])
        for i in range(5):
            print(i+1, news_art[i])
            talk(news_art[i])

    elif "weather" in command:

        # Google Open weather website
        # to get API of Open weather
        api_key = "c0db08472971c16b18a8698c074c49de"
        talk(" City name ")
        print("City name : ")
        city_name = take_command()
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(complete_url)
        x = response.json()
        print(x)

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidiy) + "\n description = " + str(weather_description))

        else:
            talk(" City Not Found ")

    elif "calculate" in command:
        app_id = "JHXUY7-VLW8HW4HQ6"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        query = command.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        talk("The answer is " + answer)

    elif 'open powerpoint' in command:
        talk("opening Power Point presentation")
        ppt = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(ppt)

    elif 'open excel' in command:
        talk("opening Excel")
        exe = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(exe)

    elif "restart" in command:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in command or "sleep" in command:
        talk("Hibernating")
        subprocess.call("shutdown / h")

    elif 'lock window' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in command:
        talk("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        talk("Recycle Bin Recycled")

    elif 'Bye eva' in command:
        sys.exit()

    elif "eva" in command:
        wish_me()

    else:
        talk('Please say the command again')


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    wish_me()
    username()

while 1:
    run_eva()
