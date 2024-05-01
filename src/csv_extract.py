# This script will read the source documents and creeate model objects (see model.py)
from model import RawData, XYPair

from abc import ABC, abstractmethod
from pathlib import Path

# Pair Builder, base abstract claqss for SeriesNPair classes
class PairBuilder(ABC):
    target_class = type[RawData] #Of a type that is an alias for an XYPair generic class.

    @abstractmethod
    def from_row(self, row: list[str]) -> RawData:
        ...

# SeriesNPair classes
class Series1PairBuilder(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # More implementation code
        return cls(row[0], row[1])

class Series2PairBuilder(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # More implementation code
        return cls(row[0], row[2])

class Series3PairBuilder(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # More implementation code
        return cls(row[0], row[3])
    
class Series4PairBuilder(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # More implementation code
        return cls(row[4], row[5])

# Extract class, does the extraction of all the pairs
class Extract:
    def __init__(self, builders: list[PairBuilder]) -> None:
        self.builders = builders

    def build_pairs(self, row: list[str]) -> list[RawData]:
        # Lambda to build PairBuilder objects and return XYPair objects built
        return [bldr.from_row(row) for bldr in self.builders]
    
# Simple Unit Test just for XYPair of type 1
def test_series1Pair() -> None:
    from unittest.mock import Mock, sentinel, call
    # Mock target class
    mock_raw_class = Mock()
    p1_builder = Series1PairBuilder()
    # Instantiate class under test, assign the mock as the target class to be used to create pair in subclass
    p1_builder.target_class = mock_raw_class
    # Call the from_row method of builder class that uses target class (mock in this case)
    xypair = p1_builder.from_row([sentinel.X, sentinel.Y])
    # Assert that the mock is called with the two argument captors as arguments
    assert mock_raw_class.mock_calls == [
        call(sentinel.X, sentinel.Y)
    ]
