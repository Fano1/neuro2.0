# from models.speechRecog import record_audio as hear
from google import genai
# import protocol.protocol as protocol
import os

file = "C:\\Users\\USER\\Desktop\\projects\\ai\\neuro2.0\\Rec-exe-diff\\current.c"
exefile = "C:\\Users\\USER\\Desktop\\projects\\ai\\neuro2.0\\Rec-exe-diff\\a.exe"
from dotenv import load_dotenv
load_dotenv()



def respond(cnt):
  key = os.getenv("GEMINI_API")
  client = genai.Client(api_key=key)
  response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= ("first be aware i am in a time crunch so i need the least amount of code without werod syntax, only send code not any complemetntary, must be simple no okay, no sure, just code in C++, also make it as small to medium so it is faster to write, execution efficiency doesnot matter " + cnt),
    )
  
  return (response.text)


def code(text, state):
  try:  
      # text = input(">> enter")
      # text = hear(threshold=500, silence_duration=2, chunk_size=512, duration_limit=60)
      # text = "2.	Write a program to open file “test.txt” created in previous question, read its content and display it on screen."
      if(text == " Turn yourself off."):
          return

      message = respond(text)
      print(f"me: {text}")
      print(f'ai: {message}')

      # if(state.lower() == "y"):

      #   print("C:\\Users\\USER\\Desktop\\projects\\neuro2.0\\current.c>> \n")
      #   protocolHandeler = protocol.ProtocolExecuteFile(file, message)
      #   protocolHandeler.WriteFile(message)
      #   protocolHandeler.Removelines()
      #   protocolHandeler.ExecuteFileC(exefile)    
      
      input("continue")
      
      
  except Exception as e:
      print("Bitch what?")
      print(e)
      
if __name__ == "__main__":
  while(1):
    coder = input("Code>>") 
    code(text= coder, state="n")