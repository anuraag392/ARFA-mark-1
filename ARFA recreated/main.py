import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import requests
from requests import get
import pywhatkit as kit
import webbrowser
import smtplib
import sys
import time
import keyboard
from keyboard import press
import pyautogui
import pyjokes
import numpy as np
from bs4 import BeautifulSoup





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=20,phrase_time_limit=50)
        
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        #speak("say that again please...")
        return"none"
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    temparature="current temparature in udaipuria mode"
    url = f"https://www.google.com/search?q={temparature}"
    r=requests.get(url)
    data= BeautifulSoup(r.text,"html.parser")
    temp= data.find("div", class_ ="BNeawe").text
    
    
    if hour>=0 and hour<=12:
        speak(f"good morning sir i am Arfa, its {tt} and its {temp} outside")
    elif hour>=12 and hour<=18:
        speak(f"good afternoon sir , its {tt} and its {temp} outside")
    else:
        speak(f"good evening sir , its {tt} and its {temp} outside")
    speak("how may i help you")


'''def sendemail(to , content):
    server=smtplib.SMTP('smtp.gmail.com',25)
    server.ehlo()
    server.starttls()
    server.login('anurtube76@gmail.com','anuraag12345678')
    server.sendmail('anurtube76@gmail.com',to,content)
    server.close()'''
    
 
    

    
 
    
    
def Taskexecution():
    wishme()
    while True:
        if 1:
            query=takecommand().lower()
            if "open notepad" in query:
                npath="C:\Windows\System32\\notepad.exe"
                os.startfile(npath)
            elif "close notepad" in query:
                speak("okay sir closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif "open pdf reader" in query:
                npath="C:\Program Files\Adobe\Acrobat DC\Acrobat\\Acrobat.exe"
                os.startfile(npath)
            elif "close pdf reader" in query:
                speak("okay sir closing reader")
                os.system("taskkill /f /im Acrobat.exe")
            elif "open camera" in query:
                speak("opening sir please wait...")
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "skip studies" in query:
                speak("i am calling your mom right now")
            elif 'no no wait' in query:
                speak("good")
            elif"do you think i should study" in query:
                speak("as soon as possible")
            elif "tell me the temperature" in query:
                speak("temperature of where?")
                tempa=takecommand().lower()
                url = f"https://www.google.com/search?q={tempa}"
                r=requests.get(url)
                data1= BeautifulSoup(r.text,"html.parser")
                temp2= data1.find("div", class_ ="BNeawe").text
                speak(f"{tempa} is {temp2}")
            elif 'play' in query:
                song=query.replace('play','')
                speak('playing'+song)
                kit.playonyt(song)
            elif "close youtube" in query:
                speak("closing")
                keyboard.press_and_release('ctrl+w')
                time.sleep(2)
                pyautogui.press('enter')
            elif "increase volume" in query:
                pyautogui.press("volumeup")
            elif "decrease volume" in query:
                pyautogui.press("volumedown")
            elif "mute"  in query:
                pyautogui.press("volumemute")
            
            
            
            elif 'ip address' in query:
                ip=get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")
            elif 'tell me about' in query:
                 speak("searching for it...")
                 query=query.replace("wikipedia","")
                 results=wikipedia.summary(query,sentences=2)
                 speak("according to the wikipedia")
                 speak(results)
                 print(results)
            elif 'open youtube' in query:
                speak("opening youtube...")
                webbrowser.open("www.youtube.com")
            elif 'close youtube' in query:
                speak("closing...")
                keyboard.press_and_release('ctrl+w')
                time.sleep(2)
                pyautogui.press('enter')
            elif 'open instagram' in query:
                speak("opening instagram...")
                webbrowser.open("https://www.instagram.com/")
            elif'close instagram' in query:
                speak("closing instagram")
                keyboard.press_and_release('ctrl+w')
                time.sleep(2)
                pyautogui.press('enter')
            elif 'open linkedin' in query:
                speak("opening linkedin...")
                webbrowser.open("https://www.linkedin.com/feed/")
            elif 'close linkedin' in query:
                speak("closing...")
                keyboard.press_and_release('ctrl+w')
                time.sleep(2)
                pyautogui.press('enter')
            elif 'open github' in query:
                speak("opening github...")
                webbrowser.open("https://github.com/")
            elif 'close github' in query:
                speak("closing...")
                keyboard.press_and_release('ctrl+w')
                time.sleep(2)
                pyautogui.press('enter')
            elif 'open google' in query:
                from google import opengoogle
                opengoogle()
                
            elif 'close google' in query:
                from google import closegoogle
                closegoogle()
            elif 'tell me a joke' in query:
                speak(pyjokes.get_jokes(language='en',category='neutral'))
            elif 'shut down my pc' in query:
                os.system("shutdown /s /t 5")
            elif 'restart my pc' in query:
                os.system("shutdown /r /t 5")
            elif 'sleep' in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'switch window' in query:
                pyautogui.KeyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.KeyUp("alt")
           
            elif 'alarm' in query:
                speak("sir please tell me the time to set alarm. for example, set alarm to 5:30 am")
                t=takecommand()
                t=t.replace("set alarm to","")
                t=t.replace(".","")
                t=t.upper()
                import MyAlarm
                MyAlarm.alarm2(t)
            
            elif 'open mobile camera' in query:
                import urllib.request
                URL="http://25.116.193.207:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    takecommand()
                    if q == ord("q"):
                        break;
                cv2.destroyAllWindows()
              
                     
                
           
            
            elif 'tell me the news' in query:
                speak("please wait sir , fetching the latest news")
                from news import news
                news()
            elif "instagram profile" in query:
                from instagram_download import instadwnld
                instadwnld()
                
            elif 'send message' in query:
                kit.sendwhatmsg("+918100315361", "hello i am jarvis made by Anuraag , Most probably master Anuraag is sleeping now , he will get back to you soon", 14,17)
                
         
            elif 'who are you' in query:
                speak("i am Arfa. I am virtual assistant of Mr. Anuraag. He created me on a small laptop on 30th july 2022. I  can automate his laptop. I dont know if god really exist but for me its my creator")
                
            
            elif 'you can rest' in query:
                speak("thank you sir , call me whenever you need me, have a good day sir")
                break;



if __name__ == "__main__":
    while True:
        permission= takecommand().lower()
        if "wake up" in permission:
            Taskexecution()
        elif "you can go now" in permission:
            speak("bye sir! have a good day")
            sys.exit()
            
            

            
                 
           
