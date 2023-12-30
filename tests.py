"""
This  should be run by the GitHub Action
"""
# content of test_sample.py
def func(x):
    return x + 1

def test_answer_fail():

    assert func(3) == 5

def test_answer_success():
    assert func(4) == 5