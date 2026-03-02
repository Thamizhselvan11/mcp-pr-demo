import math
from typing import Optional, List

def calculate_area(radius: float) -> Optional[float]:
    """Calculate the area of a circle given its radius.
    Args:
        radius: The radius of the circle (must be positive)
    Returns:
        The calculated area as a float, or None if radius is invalid (≤ 0)
    Example:
        >>> calculate_area(5)
        Area is : 78.53981633974483
        78.53981633974483
    Raises:
        ValueError: If radius is not a number
    """
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius <= 0:
        print("Invalid radius")
        return None
    area = math.pi * radius * radius
    print(f"Area is: {area}")
    return area

def process_list(items: List[int]) -> int:
    """Calculate the sum of all even numbers in the list.
    Args:
        items: A list of integers
    Returns:
        The sum of all even numbers in the list
    Example:
        >>> process_list([1, 2, 3, 4, 5, 6])
        Total: 12
        12
    Raises:
        ValueError: If any item is not an integer
    """
    if not all(isinstance(i, int) for i in items):
        raise ValueError("All items must be integers")
    total = sum(i for i in items if i % 2 == 0)
    print(f"Total: {total}")
    return total

class Student:
    """Represents a student with name and age attributes."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")