"""
This  should be run by the GitHub Action
"""
# content of test_sample.py
def func(x):
    """
    This  should be run by the GitHub Action
    """
    return x + 1

def test_answer_fail():
    """
    This  should be run by the GitHub Action
    """
    assert func(3) == 5

def test_answer_success():
    """
    This  should be run by the GitHub Action
    """
    assert func(4) == 5
  