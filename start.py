import json
import string
from flask import Flask, render_template
import tkinter as tk

app = Flask(__name__);

channels = [0, 0, 0, 0, 0]

# Start local UI
root = tk.Tk()
root.title('Channel Monitor')
root.geometry('600x400+50+50')

message = tk.Label(root, text="Hello, World!")
message.pack()

# server
@app.route('/')
def index():
    return render_template("index.html", channels=channels, enumerate=enumerate)

@app.route('/setChannel/<int:channel>/<int:level>')
def set_channel(channel, level):
    # Check to make sure params are in bounds
    if channel < 0 or channel > len(channels) - 1 or level < 0 or level > 255:
        return "Error: out of range"
    channels[channel] = level
    print(channels)
    jsonChannels = json.JSONEncoder().encode(channels)
    message['text'] = jsonChannels
    return jsonChannels

if __name__ == '__main__':
    app.debug = True
    app.run()
    
root.mainloop()