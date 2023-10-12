t tests for console using Mock module from the python standard library
Checks console for capturing stdout into a StringIO object
"""

import sys
import unittest
from unittest.mock import create_autospec
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err_messages = [
            "** class name missing **",
            "** class doesn't exist **",
            "** instance id missing **",
            "** no instance found **"
        ]

        self.class_names = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        ]

    def create_console(self):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_write(self, nr=None):
        """Returns the last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit_command(self):
        """Test quit command"""
        cli = self.create_console()
        self.assertTrue(cli.onecmd("quit"))

if __name__ == '__main__':
    unittest.main()

