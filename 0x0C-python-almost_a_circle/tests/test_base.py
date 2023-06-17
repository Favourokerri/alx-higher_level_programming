#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_id_assignment_with_positive_id(self):
        '''
            assignment with positive
        '''
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_id_assignment_with_negative_id(self):
        '''
            Assignment with negative
        '''
        obj = Base(-10)
        self.assertEqual(obj.id, -10)

    def test_id_assignment_without_id_argument(self):
        '''
            without id
        '''
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_class_docstring(self):
        '''
            doc string test
        '''
        self.assertIsNotNone(Base.__doc__)

    def test_init_docstring(self):
        '''doc string test
        '''
        self.assertIsNotNone(Base.__init__.__doc__)
