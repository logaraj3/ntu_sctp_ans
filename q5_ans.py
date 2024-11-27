def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Ensure both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")
    
    # Check if num is divisible by divisor
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    else:
        return num % divisor == 0


def test_check_divisibility():
    # Test Case 1: Check divisibility of 10 by 2
    result = check_divisibility(10, 2)
    assert result == True, "Test Case 1 Failed"

    # Test Case 2: Check divisibility of 7 by 3
    result = check_divisibility(7, 3)
    assert result == False, "Test Case 2 Failed"

# Run the tests
test_check_divisibility()
print("All test cases passed!")

