"""
Another docstring to get it past pylint - and new line at the end
"""
def main():
    """
    This is an example docstring to describe my program
    """
    print("Hello World")
    print("Goodbye world")
    print("Hello World")
    print("Goodbye world")
    print("This is from GitHub!")
    print("Its hot in B26")
    print("Changing on 30/1/23")
    print("https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions")
    a = "Hello"
    b = "GoodbyE"
    print( a + b)

main()

# content of test_sample.py
def func(x):
    return x + 1

def test_answer_fail():

    assert func(3) == 5
    
def test_answer_success():
    assert func(4) == 5
