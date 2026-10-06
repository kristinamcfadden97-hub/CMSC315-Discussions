"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each value from beginning to end.
    # In the worst case, every item is checked, so the runtime is O(n).
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 if the target is not found.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Start with the entire sorted list as the search space.
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle of the current search space.
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        # Eliminate the left half if the target is larger.
        elif lst[mid] < target:
            low = mid + 1

        # Eliminate the right half if the target is smaller.
        else:
            high = mid - 1

    # Return -1 if the target is not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted dataset.
    small_data = [55, 67, 72, 81, 90, 95]

    # Search for a value that exists using both algorithms.
    existing_target = 81
    print("Linear search for 81:", linear_search(small_data, existing_target))
    print("Binary search for 81:", binary_search(small_data, existing_target))

    # Search for a value that does not exist using both algorithms.
    missing_target = 100
    print("Linear search for 100:", linear_search(small_data, missing_target))
    print("Binary search for 100:", binary_search(small_data, missing_target))

    # Both searches return the index when a value is found.
    # Both searches return -1 when the value is not found.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a larger sorted dataset containing values from 1 through 10000.
    large_data = list(range(1, 10001))
    large_target = 9999

    # Test the same target with both search algorithms.
    print("Linear search for 9999:", linear_search(large_data, large_target))
    print("Binary search for 9999:", binary_search(large_data, large_target))

    # Linear search may check thousands of values before finding the target.
    # Binary search repeatedly cuts the search area in half, so it requires
    # far fewer comparisons as the dataset becomes larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list contains no values, so both searches return -1.
    empty_list = []
    print("Linear search on empty list:", linear_search(empty_list, 81))
    print("Binary search on empty list:", binary_search(empty_list, 81))

    # Edge case 2: A single-element list can still be searched successfully.
    single_element = [81]
    print("Linear search on single-element list:", linear_search(single_element, 81))
    print("Binary search on single-element list:", binary_search(single_element, 81))

    # Edge case 3: A missing value causes both searches to return -1.
    edge_data = [10, 20, 30, 40, 50]
    print("Linear search for missing value:", linear_search(edge_data, 35))
    print("Binary search for missing value:", binary_search(edge_data, 35))

    # ===============================
    # PERFORMANCE ANALYSIS
    # ===============================
    # Linear search has O(n) time complexity because it may need to
    # check every item before finding the target.
    # Binary search has O(log n) time complexity because each comparison
    # eliminates half of the remaining search space.

    print("\n=== PERFORMANCE ANALYSIS ===")
    print("Linear search time complexity: O(n)")
    print("Binary search time complexity: O(log n)")
    print("Binary search becomes more efficient as a sorted dataset gets larger.")

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================
    # This example represents searching for a song in a music library.
    # Linear search can search an unsorted list, while binary search
    # requires the songs to already be sorted.

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    songs = ["All The Stars", "God's Plan", "Love Galore", "Passionfruit", "Snooze"]
    song_target = "Passionfruit"

    print("Linear search for Passionfruit:", linear_search(songs, song_target))
    print("Binary search for Passionfruit:", binary_search(songs, song_target))

    # Both searches find the song, but binary search can become much faster
    # when searching a large sorted music library.


if __name__ == "__main__":
    main()