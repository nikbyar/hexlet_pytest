from example import reverse
import pytest

def test_stack():
    stack = []
    assert stack.append(1) == None

    stack.append(2)
    stack.append(3)
    assert stack.pop() == 3  
    assert stack.pop() == 2 
    
def test_emptiness():
    stack = []
    assert not stack
    stack.append('qqq')
    assert bool(stack)
    stack.pop()
    assert not stack

def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()