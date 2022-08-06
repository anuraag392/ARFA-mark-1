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


def opengoogle():
    speak("What do you want me to search for sir")
    cm=takecommand().lower()
    webbrowser.open(f"{cm}")
def closegoogle():
    speak("closing...")
    keyboard.press_and_release('ctrl+w')
    time.sleep(2)
    pyautogui.press('enter')