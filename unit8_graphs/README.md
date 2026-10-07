# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

Implementation
I created a graph using an adjacency list that represented a streaming recommendation network. Each node represented a movie or television show, while the edges represented connections based on similar genres or viewing preferences.
I implemented Breadth-First Search using a queue and a visited set. The queue allowed the graph to be searched level by level, while the visited set prevented the same node from being processed more than once. I also added another node to the graph and ran BFS again to see how the traversal changed.
For edge cases, I tested a starting node that did not exist in the graph and a graph containing only one node. The missing node returned an empty list without causing an error, while the single-node graph returned only that node.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

Reflection
This assignment helped me understand how graphs can represent relationships between different objects and how BFS can be used to move through those relationships. I learned how to create an adjacency list in Python and use a queue and visited set to control the traversal. Seeing the traversal output also helped me understand what it means for BFS to search a graph level by level.
The most challenging part was making sure nodes were not visited more than once while still adding the correct neighbors to the queue. Using a visited set made this easier because I could keep track of nodes that had already been discovered. Testing a missing starting node and a single-node graph also helped me see why edge cases are important.
BFS and DFS both traverse graphs, but they explore them differently. BFS checks nearby nodes first, while DFS follows one path as far as possible before backtracking. BFS would be useful for finding nearby connections or the shortest route in an unweighted graph. DFS could be useful when exploring deeper paths, such as following a chain of related content in a recommendation system.