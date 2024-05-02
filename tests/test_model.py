import sys
import os

from unittest.mock import sentinel
from unittest import TestCase
from dataclasses import asdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import XYPair

class TestModel(TestCase):
    # Test instantiation of the XYPair model class
    def test_xypair(self):
        pair = XYPair(x=sentinel.X, y=sentinel.Y)
        assert pair.x == sentinel.X
        assert pair.y == sentinel.Y
        assert asdict(pair) == {"x": sentinel.X, "y": sentinel.Y}
