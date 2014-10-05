class SimpleElevator():
    def __init__(self, current=0):
        self.current_floor = current
        self.has_to_close = False
        self.direction = "^"
        self.gos = []
        self.calls = []

    def reset(self, cause):
        print "reset because " + cause
        return ""

    def next_command(self):
        if self.has_to_close:
            self.has_to_close = False
            return "CLOSE"

        if self.current_floor in self.calls or self.current_floor in self.gos:
            return "OPEN"

        if is_highest_floor(self.current_floor):
            self.current_floor = self.current_floor - 1
            return "DOWN"

        if is_lowest_floor(self.current_floor):
            self.current_floor = self.current_floor + 1
            return "UP"

        if self.direction == "^":
            self.current_floor = self.current_floor + 1
            return "UP"
        if self.direction == "v":
            self.current_floor = self.current_floor - 1
            return "DOWN"

        return "NOTHING" #return "UP|DOWN|OPEN|CLOSE|NOTHING"

    def compute_direction(self, floor):
        if int(floor)- self.current_floor > 0:
            self.direction = "^"
        else:
            self.direction = "v"
    
    def go(self, floor_to_go):
        self.gos.append(int(floor_to_go))
        self.compute_direction(floor_to_go)    
        return ""

    def user_has_entered(self):
        self.has_to_close = True
        if self.current_floor in self.calls:
            self.calls.remove(self.current_floor)
        if self.current_floor in self.gos:
            self.gos.remove(self.current_floor)
        return ""

    def user_has_exited(self):
        self.has_to_close = True
        if self.current_floor in self.calls:
            self.calls.remove(self.current_floor)
        if self.current_floor in self.gos:
            self.gos.remove(self.current_floor)
        return ""

    def call(self, at_floor, floor_to_go):
        self.calls.append(int(at_floor))
        self.compute_direction(at_floor)
        return ""

def is_lowest_floor(floor):
    return floor == 0

def is_highest_floor(floor):
    return floor == 5
