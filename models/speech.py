import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')                    
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
voices = engine.getProperty('voices')       

#setting properties
engine.setProperty('rate', 150) # setting up new voice rate
engine.setProperty('volume',1.0)    
#engine.setProperty('voice', voices[0].id)  
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

