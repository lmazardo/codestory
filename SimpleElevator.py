class SimpleElevator():
    def __init__(self):
        self.current_floor = 0
    def reset(self, cause):
        print "reset because " + cause
        pass
    def next_command(self):
        if self.current_floor != 5:
            self.current_floor = self.current_floor + 1
            return "UP"
        if self.current_floor == 5:
            self.current_floor -= 1
            return "DOWN"
        return "NOTHING" #return "UP|DOWN|OPEN|CLOSE|NOTHING"
    def call(self, at_floor, floor_to_go):
        print "called at " + at_floor + " : " + "^" if floor_to_go == "UP" else "v"

