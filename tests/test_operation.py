from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,2)==6
    assert add(4+5)==9

def test_sub():
    assert sub(10,2)==8
    assert sub(7,3)==4
    assert sub(10,1)==9