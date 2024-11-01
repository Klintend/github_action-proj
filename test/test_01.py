from script.calculator import add, substract, multiply, division
from pytest import mark

@mark.parametrize("x, y, expected_result", [
    (20, 10, 10),
    (40, 30, 10)
])

def test_substract_function(x, y, expected_result):
    assert substract(x, y) == expected_result
