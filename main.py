"""
Demo module for MCP PR testing.

Contains functions for area calculation, list processing, and a student class.
Demonstrates best practices in Python code with proper formatting and documentation.
"""

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
    """
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
    """
    total = sum(i for i in items if i % 2 == 0)
    print(f"Total: {total}")
    return total


class Student:
    """Represents a student with name and age attributes.
    
    Attributes:
        name: The student's full name
        age: The student's age in years
    """
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize a Student instance.
        
        Args:
            name: The student's name
            age: The student's age
        """
        self.name = name
        self.age = age
    
    def display(self) -> None:
        """Display the student's information."""
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":
    # Example usage
    print("=== Area Calculation ===")
    calculate_area(5)
    
    print("\n=== List Processing ===")
    process_list([1, 2, 3, 4, 5, 6])
    
    print("\n=== Student Information ===")
    student1 = Student("John Doe", 20)
    student1.display()
