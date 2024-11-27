def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
  # Ensure lst is a list
    if not isinstance(lst, list):
        raise ValueError("The first argument must be a list.")
    
    # Replace occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst


def test_find_and_replace():
    # Test Case 1: Replace integers in a list
    result = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
    assert result == [1, 5, 3, 4, 5, 5], "Test Case 1 Failed"

    # Test Case 2: Replace strings in a list
    result = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
    assert result == ["orange", "banana", "orange"], "Test Case 2 Failed"


# Run the tests
test_find_and_replace()
print("All test cases passed!")
