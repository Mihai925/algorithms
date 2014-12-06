import unittest
from ..data_structures import stack

class TestStack(unittest.TestCase):

    def test_stacksize(self):
        self.stack = stack.stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.size(), 3)

        self.stack.peek()

        self.assertEqual(self.stack.size(), 3)

        self.stack.pop()
        self.stack.pop()
        self.stack.pop()

        self.assertEqual(self.stack.size(), 0)

    def test_stackempty(self):
        self.stack = stack.stack()

        self.assertTrue(self.stack.is_empty())

        self.stack.push(1)
        self.stack.push(5)

        self.assertFalse(self.stack.is_empty())

    def test_peekpush(self):
        self.stack = stack.stack()

        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        self.stack = stack.stack()

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        with self.assertRaises(IndexError): 
            self.stack.pop()
