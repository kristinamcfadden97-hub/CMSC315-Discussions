# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation Documentation

I created a parent class to represent a general smart device and a child class to represent a smart thermostat. The parent class stored the device name and status, while the child class inherited those attributes and added temperature and mode.

I demonstrated class and instance namespaces by creating multiple thermostat objects, adding an attribute to one object, and displaying the namespaces with `__dict__`.

I also demonstrated shallow and deep copying using nested thermostat settings. The shallow copy shared the nested data with the original object, while the deep copy maintained its own separate copy.

For my student-created extension, I added a `set_mode()` method that allowed the thermostat to change between operating modes. I tested the method by changing the bedroom thermostat from Heat mode to Cool mode.

As an additional test case, I tested the thermostat with a temperature of -10. The program accepted and displayed the unusual temperature value without producing an error. This demonstrated how the program handles a special-case value.

A real-world use for this program would be a smart home system that manages devices such as thermostats and smart locks. Using OOP would make it easier to add new types of smart devices while reusing common features from the parent class.
