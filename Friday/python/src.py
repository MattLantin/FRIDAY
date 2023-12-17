import os
from dotenv import load_dotenv

import time
import pyaudio
import playsound
from gtts import gTTS

import openai
import speech_recognition as sr

load_dotenv() 

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

print(OPEN_AI_KEY) 

lang ='en'

openai.api_key = OPEN_AI_KEY


guy = ""

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy 
                guy = said
                

                if "Friday" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string) 
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text = text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")
                    
            except Exception as e:
                print(f"Exception: {e}")


        return said

    if "stop" in guy:
        break


    get_adio()