import unittest
from pyconnect4.entities import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        """Tests User Creation"""

        testing_subject = User(1, "RDJ1")

        self.assertEqual(testing_subject.ID, 1, "User ID should be equal to 1")
        self.assertEqual(testing_subject.Name, "RDJ1", "User Name should be equal to RDJ1")

