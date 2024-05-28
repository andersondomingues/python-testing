from src.main import soma, subtracao

def test_soma():
    assert soma(1, 1) == 2

def test_subtracao():
    assert subtracao(1, 0) == 1
