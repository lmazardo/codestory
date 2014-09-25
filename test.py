import unittest
import SimpleElevator

class Test(unittest.TestCase):

    def setUp(self):
        print "setup"

    def test_reset_is_implemented(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.reset("normal cause")
        self.assertEquals(0, elevator.current_floor)
    def test_next_command_is_implemented(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.next_command()
    def test_call_is_implemented(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("3", "UP")
