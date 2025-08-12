import time
from plyer import notification
# from playsound import playsound

# Reminder interval in seconds (e.g., 1 hour = 3600 seconds)
reminder_interval = 60 * 60  # 1 hour

# Path to the sound file (you can use any .mp3 or .wav file)
# sound_path = "water_reminder.mp3"  # Optional sound

def remind_to_drink():
    while True:
        notification.notify(
            title="💧 Drink Water Reminder",
            message="Time to drink a glass of water! Stay hydrated.",
            timeout=10  # notification duration in seconds
        )
        # try:
        #     playsound(sound_path)
        # except:
        #     print("Sound file not found or error playing sound.")
        time.sleep(reminder_interval)

# if __name__ == "__main__":
#     print("Drink Water Reminder is running...")
remind_to_drink()
