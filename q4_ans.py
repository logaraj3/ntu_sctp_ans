def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Ensure s is a string
    if not isinstance(s, str):
        raise ValueError("The input must be a string.")
    
    # Return the reversed string
    return s[::-1]


def test_string_reverse():
    # Test Case 1: Reverse a string "Hello World"
    result = string_reverse("Hello World")
    assert result == "dlroW olleH", "Test Case 1 Failed"

    # Test Case 2: Reverse a string "Python"
    result = string_reverse("Python")
    assert result == "nohtyP", "Test Case 2 Failed"


# Run the tests
test_string_reverse()
print("All test cases passed!")
