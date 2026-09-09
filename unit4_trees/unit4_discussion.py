"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive helper compares values to decide where they belong.
        # Smaller values go left, while larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # A null position means the correct insertion spot was found.
        if node is None:
            return Node(value)

        # Values smaller than the current node belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Values larger than the current node belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the node so the tree's links remain connected after recursion.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search reduces the search space by choosing only one subtree at each step.
        # This is often more efficient than checking every value one by one.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching None means the value is not in the tree.
        if node is None:
            return False

        # If the current node contains the value, the search is complete.
        if value == node.value:
            return True

        # Smaller values can only be in the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Larger values can only be in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # In-order traversal visits left, current node, then right.
        # Because BST values are ordered left < node < right,
        # this traversal produces the values in sorted order.
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Employee IDs are used as a real-world example of values stored in a BST.
    tree = BST()
    values = [1050, 1025, 1075, 1010, 1035, 1060, 1090, 1005, 1065]

    # A BST reduces the search space by moving left for smaller values
    # and right for larger values instead of checking every value.
    for value in values:
        tree.insert(value)

    print("Employee IDs inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # In-order traversal visits left, current node, then right.
    # Since smaller values are stored on the left and larger values on the right,
    # the employee IDs are displayed in sorted order.
    sorted_values = tree.inorder()
    print("Employee IDs in sorted order:", sorted_values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # These searches demonstrate both successful and unsuccessful searches.
    # The BST chooses the left or right subtree based on the value being searched.
    print("Search for 1025:", tree.search(1025))
    print("Search for 1065:", tree.search(1065))
    print("Search for 1040:", tree.search(1040))
    print("Search for 1100:", tree.search(1100))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # An empty BST has no root, so searching it returns False
    # and its in-order traversal returns an empty list.
    empty_tree = BST()
    print("Search empty tree for 1050:", empty_tree.search(1050))
    print("Empty tree traversal:", empty_tree.inorder())

    # Duplicate values are ignored by the insertion method because
    # values are only inserted when they are smaller or larger.
    tree.insert(1050)
    print("After attempting duplicate 1050:", tree.inorder())

    # A tree with only one node should still support searching and traversal.
    single_tree = BST()
    single_tree.insert(2000)
    print("Single-node tree traversal:", single_tree.inorder())
    print("Search single-node tree for 2000:", single_tree.search(2000))



if __name__ == "__main__":
    main()