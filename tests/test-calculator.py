def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

def test_toplama():
    assert toplama(3, 4) == 7

def test_cikarma():
    assert cikarma(3, 4) == -1

def test_carpma():
    assert carpma(3, 4) == 12

def test_bolme():
    assert bolme(3, 4) == 0.75