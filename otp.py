import os
import math
import random
import smtplib
import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from translate import Translator

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("financialchatbot@gmail.com", "dpmxwocotharuzwh")
emailid = "neilzaveri26@gmail.com","saishayush@gmail.com"
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")

    bot_message = ""
    message=""

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    os.system("welcome.mp3")

    while bot_message != "Bye" or bot_message!='thanks':

        r = sr.Recognizer()  # initialize recognizer
        with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
            print("Speak Anything :")
            audio = r.listen(source)  # listen to the source
            try:
                message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
                print("You said : {}".format(message))

            except:
                print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
        if len(message)==0:
            continue
        print("Sending message now...")

        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

        print("Bot says, ",end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")

        myobj = gTTS(text=bot_message)
        myobj.save("welcome.mp3")
        print('saved')
        # Playing the converted file
        os.system("welcome.mp3")
else:
    print("Please Check your OTP again")