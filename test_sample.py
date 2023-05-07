# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5
def test_a():
    assert True

def test_b():
    a = 1
    b = 1
    c = 2
    assert a + b == c, f"{a}+{b}=={c}, 结果为真"

def test_c():
    a = 1
    b = 1
    c = 2
    assert 'abc' in "abcd"

def setup():
    print("setup执行啦")