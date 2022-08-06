import pyttsx3
import speech_recognition as sr
import datetime
import winsound


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


def alarm2(Timing):
    try:
        altime= str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
        
        altime = altime[11:-3]
        print(altime)
        Horeal = altime[:2]
        Horeal = int(Horeal)
        Mireal = altime[3:5]
        Mireal = int(Mireal)
        speak(f"Done , alarm is set for {Timing}")
        takecommand()
        while True:
            if Horeal==datetime.datetime.now().hour:
                if Mireal==datetime.datetime.now().minute:
                    print("alert!!!")
                    winsound.PlaySound('abc' , winsound.SND_LOOP)
                    
                elif Mireal<datetime.datetime.now().minute:
                    break
        takecommand()
        
    
    except:
        speak("invalid time format start by saying set alarm again")
        pass
    
    
    
          
            
