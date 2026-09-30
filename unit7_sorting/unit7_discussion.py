"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy so the original list is not changed
    sorted_list = lst.copy()

    # Go through the list multiple times
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare neighboring values
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap the values if they are out of order
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True

        # If no values were swapped, the list is already sorted
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # A list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # Create a list to hold the merged values
    result = []
    left_index = 0
    right_index = 0

    # Compare values from both lists and add the smaller value
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any values remaining in either list
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    # Return the completed sorted list
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    # Create an unsorted list of product ratings
    dataset1 = [42, 17, 83, 29, 64, 11, 55]

    # Display the original data before sorting
    print("Original list:", dataset1)

    # Sort the same dataset using both algorithms
    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    # Display the results from each sorting algorithm
    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    # Create a second dataset with different values and duplicates
    dataset2 = [75, 23, 91, 45, 23, 68, 12, 45]

    # Display the original data before sorting
    print("Original list:", dataset2)

    # Sort the same dataset using both algorithms
    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    # Display and compare the results
    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    if bubble_result2 == merge_result2:
        print("Both algorithms produced the same sorted result.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge Case 1: Empty list
    empty_list = []
    print("\nEmpty list:")
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Both algorithms safely return an empty list.")

    # Edge Case 2: Already sorted list
    sorted_list = [10, 20, 30, 40, 50]
    print("\nAlready sorted list:")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("The values remain in the same sorted order.")

    # Edge Case 3: Reverse-sorted list
    reverse_list = [50, 40, 30, 20, 10]
    print("\nReverse-sorted list:")
    print("Original:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))
    print("Both algorithms reorder the values into ascending order.")




if __name__ == "__main__":
    main()