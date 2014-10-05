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

    def test_next_command_is_up_when_call_at_3(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("3", "UP")
        next_command = elevator.next_command()
        self.assertEquals(next_command, "UP")

    def test(self):
        elevator = SimpleElevator.SimpleElevator()
        elevator.call("3", "UP")
        next_command = elevator.next_command()
        self.assertEquals(next_command, "UP")
        self.assertEquals(1, elevator.current_floor)

        next_command = elevator.next_command()
        self.assertEquals(next_command, "UP")
        self.assertEquals(2, elevator.current_floor)

        next_command = elevator.next_command()
        self.assertEquals(next_command, "UP")
        self.assertEquals(3, elevator.current_floor)

        next_command = elevator.next_command()
        self.assertEquals(next_command, "OPEN")

        elevator.user_has_entered()
        next_command = elevator.next_command()
        self.assertEquals(next_command, "CLOSE")
        
        elevator.go(0)
        next_command = elevator.next_command()
        self.assertEquals(next_command, "DOWN")
        
