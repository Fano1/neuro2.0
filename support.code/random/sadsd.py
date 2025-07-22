
from characterai import aiocai
import asyncio
import protocol.protocol as protocol

token = ""

char1 = ""
chat_id1 = ""

char2 = ""
chat_id2 = ""

message2 = " "

exectuter = protocol.ProtocolExecuteFile("C:\\Users\\USER\\Desktop\\projects\\ai\\neuro2.0\\ConverseText.py")



async def main():
    client = aiocai.Client(token)
    message2 = "Fuck you btw" 

    async with await client.connect() as chat:

        while True:
            try:  
                file = open("testhistory.txt", "a")
                
                message1 = await chat.send_message(char1, chat_id1, message2)
                print(f'{message1.name}: {message1.text}')

                message2 = await chat.send_message(char2, chat_id2, message1.text)
                print(f'{message2.name}: {message2.text}')

                            
                file.write(f'{message1.name};{message1.text} \n')
                file.write(f'{message2.name};{message2.text} \n')

                file.close()

                message2 = message2.text

            except Exception as e:
                print("Bitch what?")
                print(e)
                continue

asyncio.run(main())