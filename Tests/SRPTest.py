import unittest
import SRP
from unittest.mock import MagicMock
class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = SRP.AnimalDB()
        self.animal = SRP.Animal("Lion")

    def test_get_animal(self):
        self.db.get_animal = MagicMock(return_value=self.animal)

        result = self.db.get_animal(1)
        self.assertEqual(result, self.animal)
        self.db.get_animal.assert_called_with(1)

    def test_save_animal(self):
        self.db.save = MagicMock()
        self.db.save(1, self.animal)
        self.db.save.assert_called_with(1, self.animal)


if __name__ == '__main__':
    unittest.main()
