from flask import Flask
from flask import request

app = Flask(__name__)

import SimpleElevator
elevator = SimpleElevator.SimpleElevator()

@app.route("/nextCommand")
def nextCommand():
    global elevator
    return elevator.next_command()

@app.route("/call")
def call():
    global elevator
    return elevator.call(request.args.get("atFloor"), request.args.get("to"))

@app.route("/reset")
def reset():
    global elevator
    return elevator.reset(request.args.get("cause"))

if __name__ == "__main__":
    app.run(debug=True)

