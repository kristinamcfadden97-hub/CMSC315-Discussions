"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node is not in the graph, return an empty list.
    if start not in graph:
        return []

    # A queue is used because BFS visits nodes in the order they are discovered.
    queue = deque([start])

    # The visited set prevents the same node from being visited more than once.
    visited = {start}

    # This list stores the order in which the nodes are visited.
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Neighbors are added to the queue so BFS can visit each level
        # before moving farther away from the starting node.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS explores nodes level by level, while DFS follows one path
    # as far as possible before going back to explore another path.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents a streaming recommendation network.
    # Each node represents a movie or show, and each edge represents
    # content that is connected by similar genres or viewing preferences.
    graph = {
        "Stranger Things": ["Wednesday", "The Umbrella Academy"],
        "Wednesday": ["Stranger Things", "You"],
        "The Umbrella Academy": ["Stranger Things", "Loki"],
        "You": ["Wednesday", "Dexter"],
        "Loki": ["The Umbrella Academy", "WandaVision"],
        "Dexter": ["You"],
        "WandaVision": ["Loki"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Display each node and its connected neighbors.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # Start the traversal at Stranger Things.
    start_node = "Stranger Things"
    traversal = bfs(graph, start_node)

    # BFS first visits the starting node, then its direct neighbors,
    # followed by nodes that are farther away.
    print("Starting node:", start_node)
    print("BFS traversal:", traversal)

    # Add a new show and connect it to WandaVision.
    # Both adjacency lists are updated because the connection works
    # in both directions.
    graph["Agatha All Along"] = ["WandaVision"]
    graph["WandaVision"].append("Agatha All Along")

    # Run BFS again to show how the new node changes the traversal.
    updated_traversal = bfs(graph, start_node)
    print("\nAfter adding Agatha All Along:")
    print("Updated BFS traversal:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Try to start BFS from a node that does not exist.
    # The bfs function safely returns an empty list instead of causing an error.
    missing_node = "Breaking Bad"
    print("\nMissing start node:")
    print("BFS traversal:", bfs(graph, missing_node))

    # Edge Case 2: Test a graph containing only one node.
    # Since there are no neighbors, BFS only visits the starting node.
    single_node_graph = {
        "The Office": []
    }

    print("\nSingle-node graph:")
    print("BFS traversal:", bfs(single_node_graph, "The Office"))


if __name__ == "__main__":
    main()