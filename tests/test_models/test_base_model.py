#!/usr/bin/python3
"""the unittest for basemodel module."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """test class for BaseModel class."""
    def setUp(self):
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                     'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119434),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         '46458416-e5d5-4985-aa48-a2b369d03d2a')
        self.assertEqual(self.model2.created_at,
                         datetime(2017, 2, 10, 2, 6, 55, 258849))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_json(self):
        jsonified = str(self.model2)
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertNotIsInstance(jsonified["updated_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2017-02-10 02:06:55.258849')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
