import pyttsx3

engine = pyttsx3.init()

# Get current speaking rate
rate = engine.getProperty('rate')
print(f"Default rate: {rate}")  # usually around 200

# Set slower speaking rate
engine.setProperty('rate', 125)  # lower value = slower speed

engine.say("Hello! This is slower speech using pyttsx3.")
engine.runAndWait()
