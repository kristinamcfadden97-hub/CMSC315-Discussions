"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    lst.insert(index, value)

    # Elements at and after the index shift one position to the right.
    # Inserting near the beginning can take more time because more
    # elements must shift than when inserting near the end.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index is valid before trying to remove an item.
    if 0 <= index < len(lst):
        # Remove and return the value at the specified index.
        # Items after the removed value shift one position to the left.
        return lst.pop(index)

    # An invalid index cannot be safely removed, so return None.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Check each item in the list one at a time.
    for index in range(len(lst)):
        if lst[index] == value:
            # Return the index as soon as the value is found.
            return index

    # A linear search checks values sequentially from beginning to end.
    # If the value is not found after checking the list, return -1.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a list with several starting values.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert a value at the beginning of the list.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert a value into the middle of the list.
    insert_at(numbers, 2, 15)
    print("After inserting 15 in the middle:", numbers)

    # Insert a value at the end of the list.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Delete the first item and display the removed value.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("List after beginning deletion:", numbers)

    # Delete an item from the middle of the list.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("List after middle deletion:", numbers)

    # Delete the last item in the list.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("List after end deletion:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a value that exists in the list.
    existing_value = 20
    result = search_value(numbers, existing_value)
    print("Searching for", existing_value, "- found at index:", result)

    # Search for a value that does not exist in the list.
    missing_value = 99
    result = search_value(numbers, missing_value)
    print("Searching for", missing_value, "- result:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Try to delete using an invalid index.
    # The function should return None instead of causing an error.
    invalid_delete = delete_at(numbers, 100)
    print("Delete with invalid index:", invalid_delete)

    # Edge case 2: Try to delete from an empty list.
    # There are no valid indexes, so the function should return None.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print("Delete from empty list:", empty_delete)

    # Edge case 3: Insert a value into an empty list.
    # Index 0 is the beginning and end of an empty list.
    insert_at(empty_list, 0, 25)
    print("After inserting into empty list:", empty_list)



if __name__ == "__main__":
    main()