from characterai import aiocai
import time
from models.speech import speak 
from models.speechRecog import RECORD_PPR as hear
import pyttsx3
import subprocess as sp
import os

from dotenv import load_dotenv
load_dotenv()

#initializing variable
engine = pyttsx3.init()
rate = engine.getProperty('rate')                    
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
voices = engine.getProperty('voices')       
char = os.getenv("char_id")
token = os.getenv("usertoken")
chat_id = os.getenv("chat_id")

FilePath = "C:\\Users\\USER\\Desktop\\projects\\ai\\neuro2.0\\models\\ConverseText.py"

#setting properties
engine.setProperty('rate', 250) # setting up new voice rate
engine.setProperty('volume',1.0)    
#engine.setProperty('voice', voices[0].id)  
engine.setProperty('voice', voices[1].id)


async def main( enginer = engine):
    client = aiocai.Client(token)
    historyPath = "C:\\Users\\USER\\Desktop\\projects\\ai\\neuro2.0\\models\\history.txt" 


    async with await client.connect() as chat:

        while True:
            try:  
                file = open(historyPath, "a")
                text = hear()

                #Taking input and responding with mesage
                start = time.time()
                message = await chat.send_message(char, chat_id, text)
                print(f'{message.name}: {message.text}')
                end = time.time()

                #speaking the message
                speak(message.text, enginer)

                #putting in history
            
                file.write(f'{text},{message.name},{message.text},{(end - start)} \n')


                file.close()

            except Exception as e:
                print("Bitch what?")
                print(e)
                sp.call(["python", FilePath])

                continue

