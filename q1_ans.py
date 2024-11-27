def swap(x, y):
    """
    Swap the values of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    # Check if x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values using arithmetic operations
    x = x + y
    y = x - y
    x = x - y

    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")
    return x, y  # Return swapped values


def test_swap():
    # Test Case 1: Non-numeric input
    result = swap("Apple", 10)
    assert result == -1, "Test Case 1 Failed"

    # Test Case 2: Numeric input
    result = swap(9, 17)
    assert result == (17, 9), "Test Case 2 Failed"


# Run the tests
test_swap()
print("All test cases passed!")

