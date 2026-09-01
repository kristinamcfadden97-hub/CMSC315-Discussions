# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Reflection

For this assignment, I learned how Python lists handle insertion, deletion, and searching. I practiced inserting values at the beginning, middle, and end of a list and saw how existing elements shift when new values are added. I also used deletion with index validation so invalid positions would return None instead of causing an error. For searching, I used a linear search that checked each value one at a time until the target was found or the end of the list was reached.

One challenge I had was making sure the deletion function handled invalid indexes and empty lists safely. I solved this by checking whether the index was within the valid range before removing an item. I also tested missing search values and insertion into an empty list to make sure the program handled edge cases correctly.

List operations can affect performance depending on where changes are made. Insertions and deletions near the beginning or middle may require elements to shift, while operations near the end are often more efficient.

A real-world example of a list would be a music playlist because songs can be added, removed, searched for, and organized in a specific order.