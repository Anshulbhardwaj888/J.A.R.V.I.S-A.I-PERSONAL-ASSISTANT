import pyttsx3
import datetime
import wikipedia
import webbrowser
from requests import get
import bs4
from bs4 import BeautifulSoup
import os
import requests
import pyjokes
import pywhatkit
import pywhatkit as kit
import socket
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def temp():
    search = "temperature in delhi"
    url =f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ ="BNeawe").text
    speak(f"the temperature outside is {temperature} ")
    print(f"the temperature outside is {temperature} ")
 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am jarvis 2.0 created by Anshul bhardwaj! How may i help you")    
             
def takeCommand():
    #microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("listening....")
       r.pause_threshold = 1
       audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n") 
   
    except Exception as e:
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:

      query = takeCommand().lower() 

      if 'who is' in query:  
         
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2) 
          speak("According to Internet")
          print(results)
          speak(results)

      elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

      elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

      elif 'open gmail' in query:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)  



      elif 'open geeks for geeks' in query:
          webbrowser.open_new_tab("https://www.geeksforgeeks.org")  
          speak("geeks for geeks opened sir") 
    

      elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")     
           speak(f"Sir, the time is {strTime}")

      elif 'open vs code' in query:
          codePath = "C:\\Users\\WHITE FANG\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)
          speak(f"vs code opened")

      elif 'notepad' in query :
          codePath = "C:\\Windows\\system32\\notepad.exe"
          os.startfile(codePath)
          speak(f"notepad opened")  

      elif 'open github' in query:
          webbrowser.open("https://github.com")      

      elif 'who are you' in query or 'about you' in query or "your details" in query:
          speak("i am your personal assistant. sir, i work for you.")

      elif 'thank you' in query or 'thanks' in query:
          speak("No problem sir.")      

      elif "hello" in query or "hello Jarvis" in query:
          hel = "Hello  Sir ! How May i Help you.."
          print(hel)
          speak(hel)

      elif "how are you" in query:
          speak("fantastic Sir,how are you ?")  

      elif "i am fine" in query or "i am good"in query or "great" in query:
          speak("thats awesome .")       

      elif "who defeated thanos" in query:
          speak("Tony stark.")

      elif "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant jarvis is shutting down,Good bye')
            print('your personal assistant jarvis is shutting down,Good bye')
            break    

      elif "play " in query:
          song=query.replace("play","") 
          speak("playing" + song)
          pywhatkit.playonyt(song)

      elif 'what is' in query:  
         
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2) 
          speak("According to Internet")
          print(results)
          speak(results)    

      elif "are you single" in query:
          speak("same as you sir")    

      elif "joke" in query:
          speak(pyjokes.get_jokes())  

      elif "temperature" in query or "weather outside" in query:
          temp()

      elif "raju" in query:
          speak("pachis din mai paisa double")   

             
      
      
         



        

      

          

      