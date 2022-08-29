from re import search
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import googlescrap
import google
# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("voice assistance activated....")
    speak("hii ani ......How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("I am  an ai Assistant developed by Ani")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.co.in/")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://www.spotify.com/in-en/free/?utm_source=in-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_asia_in_premiumbusiness_core_brand_neev+contextual+in-en+google&gclid=CjwKCAjwpKyYBhB7EiwAU2Hn2co4vDLrNoEmea7yfF5RT4m6gO4VSIYJJTuGU7JrHzo1OqN5MNqcqRoCeR0QAvD_BwE&gclsrc=aw.ds")
        elif 'open WhatsApp' in query:
            speak("opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open telegram' in query:
            speak("opening Telegram")
            loc = "C:\\Users\\giria\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(loc)
        elif 'open chrome' in query:
            speak("opening chrome")
            loc = "C:\\Users\\giria\\AppData\\Local\\Google\\Chrome\\Application\\Chrome.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("https://www.youtube.com/watch?v=e52Ysc_bl_s&list=RDe52Ysc_bl_s&start_radio=1")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'tell me ' in query:
            import wikipedia as googlescrap
            speak("Searching in google ...")
            query = query.replace("google", '')
            speak("According to google")
            pywhatkit.search(query)
            
            try:
                results = googlescrap.summary(query,3)
                speak(results)
                
            
            except:
                speak("No speakable data available")
                
        elif 'exit' in query:
            exit(0)
