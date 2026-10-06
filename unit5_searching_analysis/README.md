# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Implementation Summary
I implemented both linear search and binary search algorithms in Python. The linear search checked each item from beginning to end, while the binary search repeatedly divided the search area in half. I tested both algorithms using small and large sorted datasets.
I also tested several edge cases, including an empty list, a single-element list, and a value that was not present. Both algorithms returned -1 when the target could not be found.
For the real-world scenario, I used a sorted music library and searched for a specific song using both algorithms. I also compared the performance of the two algorithms. Linear search had O(n) time complexity, while binary search had O(log n) time complexity and became more efficient as the sorted dataset grew larger.