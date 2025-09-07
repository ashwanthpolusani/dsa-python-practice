import pytest
# Import the function to be tested from your implementation file
from balanced_paranthesis import bal_paranthesis

# Test simple balanced cases
def test_balanced_simple():
    assert bal_paranthesis("()") == "balanced"
    assert bal_paranthesis("[]") == "balanced"
    assert bal_paranthesis("{}") == "balanced"

# Test nested balanced cases
def test_balanced_nested():
    assert bal_paranthesis("({[]})") == "balanced"
    assert bal_paranthesis("(({}))") == "balanced"
    assert bal_paranthesis("{[()]}") == "balanced"

# Additional test cases
def test_unbalanced():
    assert bal_paranthesis("(") == "Not Balanced"
    assert bal_paranthesis("[}") == "Not balanced"
    assert bal_paranthesis("((()") == "Not Balanced"
    assert bal_paranthesis("}{") == "Not balanced"

def test_empty():
    assert bal_paranthesis("") == "balanced"

def test_mixed_unbalanced():
    assert bal_paranthesis("([{]})") == "Not balanced"
    assert bal_paranthesis("{[}") == "Not balanced"
    assert bal_paranthesis("((][))") == "Not balanced"

# To run the tests:
# 1. Save both the implementation file (balanced_paranthesis.py) and test file (test_balanced_paranthesis.py)
# 2. Open terminal/command prompt
# 3. Navigate to the directory containing both files
# 4. Run: pytest test_balanced_paranthesis.py -v

# The -v flag gives verbose output showing which tests passed/failed
# If tests pass, you'll see green dots/PASSED
# If tests fail, you'll see red F's/FAILED with details about what went wrong
