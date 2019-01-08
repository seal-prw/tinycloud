from flask import Flask
from blinkt import set_pixel, set_brightness, show, clear, time
import socket

app = Flask(__name__)

@app.route('/')

def hello_world():
        str1 = "This is container : "
        str2 = socket.gethostname()
        str3 = str2.split('_')[1]
        str4 = int(str3)
        set_brightness(0.1)
        clear()
        set_pixel(str4, 255, 255, 255)
        show()
        time.sleep(1)

        return str1 + str3 + "\n"

if __name__ == "__main__":
        app.run(host='0.0.0.0')