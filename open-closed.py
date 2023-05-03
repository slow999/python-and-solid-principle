# Python sample codes that explains open-close principle.
# Certainly! The Open-Closed Principle (OCP) states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. In other words, you should be able to add new functionality to a software component without modifying its existing code. Here's an example in Python that demonstrates the Open-Closed Principle:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total

# Usage
calculator = AreaCalculator(shapes)
total_area = calculator.total_area()
print("Total Area:", total_area)


# In this example, we have the Shape abstract base class that defines the contract for calculating the area of different shapes. It has a single abstract method area() that needs to be implemented by its subclasses.
# The Rectangle and Circle classes extend the Shape class and provide their own implementations of the area() method.
# The AreaCalculator class takes a list of shapes and calculates the total area by iterating over the shapes and calling their area() methods. It doesn't need to be modified when new shapes are added; you can simply create a new shape class that extends Shape and implement its area() method.
# By following the Open-Closed Principle, we can add new shapes to the system without modifying the existing code. This promotes code reusability, maintainability, and allows for easy extension of functionality.
