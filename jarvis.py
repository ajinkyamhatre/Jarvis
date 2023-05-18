from pylib.voicelib import say, recognize_audio
from pylib.chatgptlib import ask_chatGPT

print("I am Jarvis 2.0!")

while True:
    recognized_audio = recognize_audio()
    if recognized_audio == "stop":
        break
    if recognized_audio:
        answer = ask_chatGPT(recognized_audio)
        say(answer)
