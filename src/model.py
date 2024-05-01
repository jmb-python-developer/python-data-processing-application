# SCript holds the definition of the Model objects (output objects)
# As represented by XPair DataClass
from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class XYPair:
    x: str
    y: str

@dataclass
class SomeOtherStructure:
    x: list[str]
    y: list[str]


#As alternative classes are added, the definition of RawData Type Alias can be expanded.
RawData: TypeAlias | SomeOtherStructure
