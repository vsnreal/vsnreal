import threading
from playsound import playsound
import time

def cheer_up():
    playsound('ulooklonely.mp3')

def user_interaction():
    print("You look lonely.")
    a = input("Am i true? (yes/no) ")
    if a.lower() in ("yes", "y", "evet", "e"):
        print("Fixing...")
        print("Oh.. Umm. This is my YouTube Channel, don't forget to sub plz. :^3")
        print("youtube.com/@vsnreal")

        # Start cheer_up in a separate thread
        cheer_up_thread = threading.Thread(target=cheer_up)
        cheer_up_thread.start()

        time.sleep(18)
        print("You look lonely.")
        time.sleep(3)
        print("I can fix that.")
        time.sleep(11)
        print("if sad():")
        time.sleep(0.2)
        print("  sad.stop()")  # Placeholder, assuming you have a stop function for playsound
        time.sleep(0.2)
        print("  beAwesome()")
        time.sleep(0.5)
        print("  exit()")
        time.sleep(0.3)
        print("\nU will be feel better than before starting this :)")
        exit()
    else:
        print("OK. Cya!")
        exit()

# Run user interaction in the main thread
user_interaction()
