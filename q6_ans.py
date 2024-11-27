def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Initialize the index to 0
    index = 0
    
    # Use a while loop to iterate through the list
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]  # Return the first negative number found
        index += 1  # Move to the next element
    
    # If no negative number is found
    return "No negatives"


def test_find_first_negative():
    # Test Case 1: List with negative numbers
    result = find_first_negative([3, 5, -1, 7, -2, 8])
    assert result == -1, "Test Case 1 Failed"
    
    # Test Case 2: List with no negative numbers
    result = find_first_negative([2, 10, 7, 0])
    assert result == "No negatives", "Test Case 2 Failed"


# Run the tests
test_find_first_negative()
print("All test cases passed!")


