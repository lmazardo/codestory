import unittest
import SimpleElevator

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_reset_is_implemented_and_returns(self):
        elevator = SimpleElevator.SimpleElevator()
        empty_response = elevator.reset("normal cause")
        self.assertEquals(0, elevator.current_floor)
        self.assertEquals("", empty_response)

    def test_next_command_is_implemented(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.next_command()

    def test_call_is_implemented_and_returns(self):
        elevator = SimpleElevator.SimpleElevator()
        empty_response = elevator.call("3", "UP")
        self.assertEquals("", empty_response)
        self.assertEquals("^", elevator.direction)

    def test_can_go_higher_than_highest_floor(self):
        elevator = SimpleElevator.SimpleElevator(5)
        elevator.call("6", "nothing")
        next_command = elevator.next_command()
        self.assertNotEquals(next_command, "UP")

    def test_can_go_lower_than_lowest_floor(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("-1", "nothing")
        next_command = elevator.next_command()
        self.assertNotEquals(next_command, "DOWN")

    def test_next_command_is_up_when_calling_at_3(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("3", "UP")
        next_command = elevator.next_command()
        self.assertEquals(next_command, "UP")

    def test_user_can_entered_when_calling_at_3(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("3", "UP")
        self.assertNextCommand(elevator, "UP")
        self.assertEquals(1, elevator.current_floor)

        self.assertNextCommand(elevator, "UP")
        self.assertEquals(2, elevator.current_floor)

        self.assertNextCommand(elevator, "UP")
        self.assertEquals(3, elevator.current_floor)

        self.assertNextCommand(elevator,"OPEN")

        elevator.user_has_entered()
        self.assertNextCommand(elevator, "CLOSE")
        
        elevator.go(0)
        self.assertNextCommand(elevator, "DOWN")
        
    def assertNextCommand(self, elevator, expected):
        self.assertEquals(elevator.next_command(), expected)
        
