import json
import string
from traceback import print_tb
from flask import Flask, render_template, request
import tkinter as tk

app = Flask(__name__)

channels = [0, 0, 0, 0, 0]

# Start local UI
root = tk.Tk()
root.title('Channel Monitor')
root.geometry('600x400+50+50')

message = tk.Label(root, text="Hello, World!")
message.pack()


def handle_command(stringCommand, arrayCommand):
    simplifiedCommandArray = stringCommand.split(' ')
    
    if simplifiedCommandArray[0] == "Chan" and simplifiedCommandArray[2] == "@" and int(simplifiedCommandArray[1]) < len(channels) and int(simplifiedCommandArray[3]) >= 0 and int(simplifiedCommandArray[3]) <= 100:
        channels[int(simplifiedCommandArray[1])] = int(simplifiedCommandArray[3])

    return channels


# server
@app.route('/')
def index():
    return render_template("index.html", channels=channels, enumerate=enumerate)


@app.route('/setChannel/<int:channel>/<int:level>')
def set_channel(channel, level):
    # Check to make sure params are in bounds
    if channel < 0 or channel > len(channels) - 1 or level < 0 or level > 100:
        return "Error: out of range"
    channels[channel] = level
    print(channels)
    jsonChannels = json.JSONEncoder().encode(channels)
    message['text'] = jsonChannels
    return jsonChannels


@app.route('/consoleCommand', methods=['POST'])
def console_command():
    body = request.get_json()
    print(body)
    return json.JSONEncoder().encode(handle_command(body['text'], body['symbols']))
    

if __name__ == '__main__':
    app.debug = True
    app.run()

root.mainloop()
