import subprocess

from gtts import gTTS

import os
import pyttsx3
engine = pyttsx3.init()

engine.say('This is a text phrase')
engine.runAndWait()