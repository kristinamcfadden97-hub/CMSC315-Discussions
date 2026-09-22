"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    # This dictionary represents an online store inventory.
    # Each SKU is a key, and the quantity in stock is the value.
    # Python dictionaries behave like hash tables by hashing each key
    # to efficiently store and retrieve its associated value.
    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 25
    inventory["P400"] = 12
    inventory["P500"] = 30


    print("\n=== INSERT OPERATIONS ===")
    print("Inventory after inserting five products:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # The SKU is used as the key to quickly retrieve its quantity.
    # Dictionary lookups are efficient because Python hashes the key.
    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    # Assigning a new value to an existing key updates the value
    # instead of creating a duplicate key.
    print("Inventory before update:", inventory)
    inventory["P100"] = 20
    print("Inventory after updating P100 to 20:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # Removing a key deletes both the SKU and its associated quantity.
    print("Inventory before deletion:", inventory)
    del inventory["P200"]
    print("Inventory after deleting P200:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: get() safely returns None when a SKU does not exist.
    missing_quantity = inventory.get("P999")
    print("Lookup for missing P999:", missing_quantity)

    # Edge case 2: pop() with a default value safely handles a missing SKU
    # without causing an error or changing the inventory.
    removed_item = inventory.pop("P999", None)
    print("Attempt to delete missing P999:", removed_item)
    print("Inventory after missing-key deletion attempt:", inventory)



if __name__ == "__main__":
    main()