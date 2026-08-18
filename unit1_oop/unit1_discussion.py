"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    device_type = "Smart Device"

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def display_info(self):
        return f"Device: {self.name}, Status: {self.status}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    device_category = "Smart Thermostat"

    def __init__(self, name, status, temperature, mode):
        super().__init__(name, status)
        self.temperature = temperature
        self.mode = mode

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature
    # Student-created extension: allows the thermostat mode to be changed.
    def set_mode(self, new_mode):
        self.mode = new_mode
    def display_info(self):
        return (f"Device: {self.name}, Status: {self.status}, "
                f"Temperature: {self.temperature}, Mode: {self.mode}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")
    device1 = ChildClass("Living Room Thermostat", "On", 72, "Heat")
    device2 = ChildClass("Bedroom Thermostat", "Off", 68, "Cool")

    print("Class variable through class:", ChildClass.device_category)
    print("Class variable through object:", device1.device_category)

    device1.location = "Living Room"

    print("Device 1 namespace:", device1.__dict__)
    print("Device 2 namespace:", device2.__dict__)
    print("Class namespace:", ChildClass.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = {
        "device": "Thermostat",
        "settings": {
            "temperature": 72,
            "mode": "Heat"
        }
    }
    shallow_copy = copy(original)
    deep_copy = deepcopy(original)
    original["settings"]["temperature"] = 75
    print("Original:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

    # A shallow copy shares nested objects with the original.
    # A deep copy creates separate copies of the nested objects.
# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent_device = ParentClass("Smart Lock", "On")
    print(parent_device.display_info())

    child_device = ChildClass("Bedroom Thermostat", "On", 70, "Heat")
    print(child_device.display_info())

    child_device.set_mode("Cool")
    print(child_device.display_info())
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()