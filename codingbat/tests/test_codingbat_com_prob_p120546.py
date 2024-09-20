import pytest
from ..codingbat_com_prob_p120546 import monkey_trouble

@pytest.mark.parametrize("a_smile, b_smile, result", [
    (False, False, True),
    (True, False, False),
    (False, True, False),
    (True, True, True)
    ])
def test_monkey_trouble(a_smile, b_smile, result):
    assert monkey_trouble(a_smile, b_smile) is result