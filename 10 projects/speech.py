import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Ask user to type something
text = input("Enter the text you want to convert to speech: ")

# Speak the text
engine.say(text)
engine.runAndWait()
