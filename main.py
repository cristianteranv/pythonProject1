""" Content of calculator """
def inc(x_value):
    """ increments by 1 """
    return x_value + 1

def test_answer():
    """ tests that inc() is working properly """
    assert inc(4) == 5
