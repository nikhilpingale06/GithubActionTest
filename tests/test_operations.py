from src.math_operations import add,sub

def test_add():
    assert add(3,5)==8
    assert add(3,6)==9
    assert add(8,5)==13

def test_sub():
    assert sub(8,3)==5
    assert sub(2,1)==1
    assert sub(8,9)==-1