"""
This  should be run by the GitHub Action
"""


# content of test_sample.py
def func(x):
  """
    This  should be run by the GitHub Action
    """
  return x + 1


def test_answer_success2():
  """
    This  should be run by the GitHub Action
    """
  assert func(3) == 4  # should pass now


def test_answer_success():
  """
    This  should be run by the GitHub Action
    """
  assert func(4) == 5
