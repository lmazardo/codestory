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

@app.route("/userHasEntered")
def user_has_entered():
    global elevator
    return elevator.user_has_entered()

@app.route("/go")
def go():
    global elevator
    return elevator.go(request.args.get("floorToGo"))
    
@app.route("/userHasExited")
def user_has_exited():
    global elevator
    return elevator.user_has_exited()

if __name__ == "__main__":
    app.run(debug=True)

