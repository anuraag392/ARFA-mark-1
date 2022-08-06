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
import instaloader
import instadownloader


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
        audio=r.listen(source,timeout=5,phrase_time_limit=8)
        
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        #speak("say that again please...")
        return"none"
    return query

def instadwnld():
    speak("sir please enter the username")
    name= input(" enter the username : ")
    webbrowser.open(f"www.instagram.com/{name}")
    speak("here is the profile sir")
    time.sleep(5)
    speak("sir should i download the profile for future references ?")
    condition= takecommand().lower()
    if "yes" or "ok" in condition:
        mod = instaloader.Instaloader()
        mod.download_profile(name , profile_pic_only=True)
        speak("done sir!")
    else:
        pass
    