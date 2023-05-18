# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()


# Function to convert text to
# speech
def say(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def recognize_audio():
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = recognizer.listen(source2)

            # Using google to recognize audio
            recognized_text = recognizer.recognize_google(audio2)
            recognized_text = recognized_text.lower()
            print("Did you say? ", recognized_text)
            return recognized_text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")


# Loop infinitely for user to
# speak
if __name__ == "__main__":
    while True:
        cmd = recognize_audio()
        if cmd:
            say(cmd)
