from flask import Flask
from flask import request

current_floor=0
app = Flask(__name__)

@app.route("/nextCommand")
def nextCommand():
    global current_floor
    if current_floor != 5:
        current_floor = current_floor + 1
        return "UP"
    if current_floor == 5:
        current_floor -= 1
        return "DOWN"
    return "NOTHING"
    #return "UP|DOWN|OPEN|CLOSE|NOTHING"

@app.route("/call")
def call():
    print "call at "+ request.args.get("atFloor") + " to " + request.args.get("to")
    return ""

@app.route("/reset")
def reset():
    global current_floor
    current_floor=0
    print "reset : " + request.args.get("cause")
    return ""

if __name__ == "__main__":
    current_floor=0
    app.run(debug=True)

