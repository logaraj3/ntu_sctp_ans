def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the original value
        print(f"Original value of '{key}': {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct


def test_update_dictionary():
    # Test Case 1: Adding a new key-value pair to an empty dictionary
    result = update_dictionary({}, "name", "Alice")
    assert result == {"name": "Alice"}, "Test Case 1 Failed"

    # Test Case 2: Updating an existing key-value pair
    result = update_dictionary({"age": 25}, "age", 26)
    assert result == {"age": 26}, "Test Case 2 Failed"


# Run the tests
test_update_dictionary()
print("All test cases passed!")

