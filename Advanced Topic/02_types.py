from typing import List, Tuple, Dict, Union

# n : int = 5


# name: str = "Arijit"

# def sum(a: int, b: int) -> int:
#     return a + b

#List of integers
numbers: list[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary of a string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Arijit": 99}

#Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID102"
identifier = 12345

# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.
